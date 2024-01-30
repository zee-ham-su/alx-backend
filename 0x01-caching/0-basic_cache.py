#!/usr/bin/python3
""" module for class BasicCache that
inherits from BaseCaching
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class
    """
    def __init__(self):
        """  initializing the class """
        super().__init__()

    def put(self, key, item):
        """  assign to the dictionary self.cache_data the item
        value for the key """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """  return the value that is linked to the key """
        if key and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
