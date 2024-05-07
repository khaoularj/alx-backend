#!/usr/bin/python3
"""LRUCache that inherits from
BaseCaching and is a caching system"""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """class that implement a LRUCache
    cache system that inherits from BaseCaching"""

    def __init__(self):
        """method that initliaze LRUCashe class"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """method that assign the
        value of 'item' to the key 'key' in the cache"""
        if key is None or item is None:
            return

        elif key and item:
            if self.cache_data.get(key):
                self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item

            if len(self.queue) > self.MAX_ITEMS:
                old_key = self.queue.pop(0)
                self.cache_data.pop(old_key)
                print('DISCARD: {}'.format(old_key))

    def get(self, key):
        """method that return the value
        stored in the cache for the given key"""
        value = self.cache_data.get(key)
        if value is not None:
            self.queue.remove(key)
            self.queue.append(key)
        return value
