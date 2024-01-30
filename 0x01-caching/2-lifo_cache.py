#!/usr/bin/python3
"""this is a module of class LIFOCache
that inherits from BaseCaching"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.insertion_order = []

    def put(self, key, item):
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    discarded_element = self.insertion_order.pop()
                    del self.cache_data[discarded_element]
                    print("DISCARD: {}".format(discarded_element))
                self.insertion_order.append(key)
                self.cache_data[key] = item

    def get(self, key):
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
