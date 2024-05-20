#!/usr/bin/env python3
import csv
import math
from typing import List

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
        """
        Retrieves the specified page of data from the dataset.

        Args:
            page (int): The 1-indexed page number (default is 1).
            page_size (int): The number of items per page (default is 10).

        Returns:
            List[List]: The list of rows corresponding to the requested page.
        """
        assert isinstance(page, int) and page > 0, "Page must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer."

        dataset = self.dataset()
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        
        try:
            return dataset[start_index:end_index]
        except IndexError:
            return []