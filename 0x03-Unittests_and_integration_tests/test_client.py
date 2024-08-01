#!/usr/bin/env python3

""" Unit tests for GithubOrgClient """
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock, Mock
from client import GithubOrgClient
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

    @parameterized.expand(["google", "abc"])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        expected_payload = {"payload": True}
        mock_get_json.return_value = expected_payload

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected_payload)
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test that _public_repos_url returns the expected URL"""
        mock_org.return_value = {"repos_url": "http://example.com/repos"}
        client = GithubOrgClient("test_org")
        self.assertEqual(client._public_repos_url, "http://example.com/repos")
        mock_org.assert_called_once()

    @patch("client.get_json")
    @patch("client.GithubOrgClient._public_repos_url", new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test that public_repos returns the expected list of repos"""
        mock_public_repos_url.return_value = "http://example.com/repos"
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]

        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(), ["repo1", "repo2", "repo3"])
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with("http://example.com/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that has_license returns the expected result"""
        client = GithubOrgClient("test_org")
        self.assertEqual(client.has_license(repo, license_key), expected)

@parameterized_class([
    {
        "org_payload": {"repos_url": "http://example.com/org"},
        "repos_payload": [
            {"name": "repo1", "license": {"key": "apache-2.0"}},
            {"name": "repo2", "license": {"key": "other"}},
            {"name": "repo3", "license": {"key": "apache-2.0"}},
        ],
        "expected_repos": ["repo1", "repo3"],
        "apache2_repos": ["repo1", "repo3"]
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Set up class method to start patcher"""
        cls.get_patcher = patch("requests.get", side_effect=cls.get_side_effect)
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down class method to stop patcher"""
        cls.get_patcher.stop()

    @classmethod
    def get_side_effect(cls, url):
        """Side effect method for requests.get"""
        if url == "http://example.com/org":
            return Mock(json=lambda: cls.org_payload)
        elif url == "http://example.com/repos":
            return Mock(json=lambda: cls.repos_payload)
        return None

    def test_public_repos(self):
        """Test public_repos method"""
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos method with license filter"""
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(license="apache-2.0"), self.apache2_repos)

if __name__ == "__main__":
    unittest.main()
