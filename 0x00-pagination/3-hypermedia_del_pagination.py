#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieves a dictionary containing pagination information for the specified index and page size.

            Args:
        index (int, optional): The start index of the page. If None, it defaults to 0.
        page_size (int): The number of items per page (default is 10).

    Returns:
        dict: A dictionary containing pagination information.
        """
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer."

        if index is None:
            index = 0

        indexed_dataset = self.indexed_dataset()
        keys = sorted(indexed_dataset.keys())

        if index < 0 or index >= len(keys):
            return {
                "index": None,
                "next_index": None,
                "page_size": page_size,
                "data": []
            }

        start_index = keys[index]
        end_index = start_index + page_size
        data = []

        for i in range(start_index, end_index):
            if i in indexed_dataset:
                data.append(indexed_dataset[i])

        next_index = end_index if end_index < len(keys) else None

        return {
            "index": start_index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data
        }