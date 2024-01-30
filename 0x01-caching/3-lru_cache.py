#!/usr/bin/python3
""" module for class LRU cache
that inherits from BaseCaching """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRU cache class """

    def __init__(self):
        """  initializing the class """
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """ assign to the dictionary self.cache_data"""
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.usage_order.remove(key)
                self.usage_order.append(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    discarded_element = self.usage_order.pop(0)
                    del self.cache_data[discarded_element]
                    print("DISCARD: {}".format(discarded_element))
                self.usage_order.append(key)
                self.cache_data[key] = item

    def get(self, key):
        """ return the value linked to key """
        if key and key in self.cache_data:
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        return None
