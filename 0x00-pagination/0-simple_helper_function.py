#!/usr/bin/env python3
"""function that takes two integer arguments page and page_size"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """this function return a tuple of size
    two containing a start index and an end index"""
    start = page * page_size - page_size
    end = page * page_size

    return (start, end)
