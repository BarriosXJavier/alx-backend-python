#!/usr/bin/env python3

"""add type annotations to the function"""

from typing import TypeVar, Mapping, Optional

T = TypeVar('T')

def safely_get_value(dct: Mapping[str, T], key: str, default: Optional[T] = None) -> Optional[T]:
    """
    Return the value for `key` if `key` is in the dictionary, otherwise return `default`.

    Parameters:
    dct (Mapping[str, T]): A dictionary with string keys and values of any type.
    key (str): The key to look for in the dictionary.
    default (Optional[T]): The default value to return if `key` is not in the dictionary.

    Returns:
    Optional[T]: The value associated with `key` if it exists, otherwise `default`.
    """


    if key in dct:
        return dct[key]
    else:
        return default
