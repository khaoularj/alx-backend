#!/usr/bin/python3
"""LIFOCache that inherits from
BaseCaching and is a caching system"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """class that implement a LIFO
    cache system that inherits from BaseCaching"""

    def __init__(self):
        """method that initliaze LIFOCashe class"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """method that assign the
        value of 'item' to the key 'key' in the cache"""
        if key is None or item is None:
            return

        elif key and item:
            if self.cache_data.get(key):
                self.stack.remove(key)
            if len(self.stack) >= self.MAX_ITEMS:
                old_key = self.stack.pop()
                self.cache_data.pop(old_key)
                print('DISCARD: {}'.format(old_key))

            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """method that return the value
        stored in the cache for the given key"""
        return self.cache_data.get(key)
