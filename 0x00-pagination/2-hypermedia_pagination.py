#!/usr/bin/env python3
import math

class Server:
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
    Retrieves a dictionary containing pagination information for the specified page and page size.

    Args:
        page (int): The 1-indexed page number (default is 1).
        page_size (int): The number of items per page (default is 10).

    Returns:
        dict: A dictionary containing pagination information.
        """
        assert isinstance(page, int) and page > 0, "Page must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer."

        dataset = self.dataset()
        total_items = len(dataset)
        total_pages = math.ceil(total_items / page_size)

        start_index = (page - 1) * page_size
        end_index = start_index + page_size

        try:
            data = dataset[start_index:end_index]
        except IndexError:
            data = []

        next_page = page + 1 if end_index < total_items else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }