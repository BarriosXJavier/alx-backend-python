#!/usr/bin/env python3

"""Mypy for validation"""

from typing import Tuple, List, Union

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    """
    Return a new tuple with each element in the input tuple repeated `factor` times.

    Parameters:
    lst (Tuple[int, ...]): A tuple of integers.
    factor (int): The number of times each element should be repeated.

    Returns:
    Tuple[int, ...]: A new tuple with each element repeated `factor` times.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return tuple(zoomed_in)

array = (12, 72, 91)  # Changed to tuple

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Corrected the factor to be an integer
