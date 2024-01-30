#!/usr/bin/python3
""" module for class FIFOCache that
inherits from BaseCaching"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ a caching information class
    """
    def __init__(self):
        """ initialize the class
        """
        super().__init__()
        self.waiting_list = []

    def put(self, key, item):
        """ assign to the dictionary self.cache_data the item
        value for the key
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    discarded_element = self.waiting_list.pop(0)
                    del self.cache_data[discarded_element]
                    print("DISCARD: {}".format(discarded_element))
                self.waiting_list.append(key)
                self.cache_data[key] = item

    def get(self, key):
        """ return the value that is linked to the key
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None


