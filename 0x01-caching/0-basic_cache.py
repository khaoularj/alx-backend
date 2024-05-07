#!/usr/bin/python3
"""Create a class BasicCache that inherits
from BaseCaching and is a caching system"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """this class  inherits from BaseCaching
    and is a caching system"""

    def put(self, key, item):
        """method that assign the value of
        'item' to the key 'key' in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """method that return the value
        stored in the cache for the given key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
