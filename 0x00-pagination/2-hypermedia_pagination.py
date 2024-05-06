#!/usr/bin/env python3
"""Implement a method named get_page that takes two integer arguments
page with default value 1 and page_size with default value 10"""
import csv
import math
from typing import List


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returns A list of rows representing the requested page of data
        or an empty list if the requested page is out of range"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        index = index_range(page, page_size)
        start = index[0]
        end = index[1]

        try:
            return self.dataset()[start:end]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """returns a dictionary containing
        hypermedia information about the page"""
        data = self.get_page(page, page_size)
        total = math.ceil(len(self.dataset()) / page_size)
        Next = page + 1 if page < total else None
        prev = page - 1 if page > 1 else None
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": Next,
            "prev_page": prev,
            "total_pages": total
        }
