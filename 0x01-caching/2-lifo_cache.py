#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching
from collections import OrderedDict
class LIFOCache(BaseCaching):
    """Create a class LIFOCache that inherits from BaseCaching and is a caching system"""

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard_key, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {discard_key}")

        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key, last=False)
        return self.cache_data[key]