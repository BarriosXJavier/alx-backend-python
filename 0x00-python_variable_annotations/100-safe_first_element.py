#!/usr/bin/env python3

""" correct duck-typed annotations """
from typing import Optional, Any, Sequence

def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Return the first element of the list if it exists, otherwise return None.

    Parameters:
    lst (Sequence[Any]): A sequence of any type of elements.

    Returns:
    Optional[Any]: The first element of the list if it exists, otherwise None.
    """


    if lst:
        return lst[0]
    else:
        return None

