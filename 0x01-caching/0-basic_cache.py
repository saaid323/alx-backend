#!/usr/bin/env python3
""" BaseCaching module
"""
BaseCaching = __import__('baseCache').BaseCaching


class BasicCache(BaseCaching):
    '''inherits from BaseCaching and is a caching system'''

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        '''does nothing if key or item is none else adds them to the
        dictionary'''
        if key is not None or item is not None:
            self.cache_data[key] = item
            return self.cache_data

    def get(self, key):
        '''returns the item from the dictionary or none'''
        if self.cache_data.get(key) is None:
            return None
        return self.cache_data[key]