#!/usr/bin/env python3
"""Create a class BasicCache
that inherits from BaseCaching and is a caching system"""

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """
    Defines a class for caching information in key-value pairs
    Methods:
        put(key, item) - store a key-value pair
        get(key) - retrieve the value associated with a key
    """
    
    """BasicCache class that inherits from BaseCaching"""
    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
        else:
            pass

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key, None)