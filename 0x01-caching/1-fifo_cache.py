#!/bin/usr/env python3
"""Create a class FIFOCache that inherits
from BaseCaching and is a caching system:"""
from base_caching import BaseCaching
from collections import deque, OrderedDict


class FIFOCache(BaseCaching):
    """
        Initializes a new instance of the FIFOCache class.

        This method calls the __init__ method of the parent class BaseCaching to initialize the inherited properties.
        It also initializes the cache_data property as an empty OrderedDict.

        Parameters:
            None

        Returns:
            None
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard_key, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {discard_key}")
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]