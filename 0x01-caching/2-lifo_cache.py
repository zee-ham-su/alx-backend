#!/usr/bin/python3
"""this is a module of class LIFOCache
that inherits from BaseCaching"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ a caching class that inherits from BaseCaching
    """
    def __init__(self):
        super().__init__()
        self.insertion_order = []

    def put(self, key, item):
        """ assign to the dictionary self.cache_data the item
        value for the key"""
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
        """ return the value that is linked to the key"""
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
