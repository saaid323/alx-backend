#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''inherits from BaseCaching and is a caching system'''

    def __init__(self):
        '''Initiliaze the class'''
        super().__init__()

    def put(self, key, item):
        '''does nothing if key or item is none else adds them to the
        dictionary'''
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        '''returns the item from the dictionary or none'''
        if key is not None or key in self.cache_data:
            return self.cache_data.get(key)
        return None
