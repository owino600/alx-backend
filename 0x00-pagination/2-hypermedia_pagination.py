#!/usr/bin/env python3
import math

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