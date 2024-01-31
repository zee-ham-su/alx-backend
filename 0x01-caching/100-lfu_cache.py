#!/usr/bin/python3
""" module for class LFUCache that
inherits from BaseCaching
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ class LFUCache
    """

    def __init__(self):
        """initializing the class"""
        super().__init__()
        self.usg_cont = {}

    def put(self, key, item):
        """ assign to the dictionary self.cache_data"""
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.usg_cont[key] += 1
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    min_usage = min(self.usg_cont.values())
                    least_frequent_keys = [
                        k for k, v in self.usg_cont.items() if v == min_usage]

                    lru_key = min(least_frequent_keys,
                                  key=lambda k: self.cache_data[k])

                    del self.cache_data[lru_key]
                    del self.usg_cont[lru_key]
                    print("DISCARD: {}".format(lru_key))

                self.cache_data[key] = item
                self.usg_cont[key] = 1

    def get(self, key):
        """ return the value linked to key """
        if key and key in self.cache_data:
            self.usg_cont[key] += 1
            return self.cache_data[key]
        return None
