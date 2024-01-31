#!/usr/bin/env python3
'''implements Lifo cache system'''
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''inherits from BaseCaching and is a caching system'''
    lis = []

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        '''adds item to a dictionary'''
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            if self.cache_data.get(key) is not None:
                self.cache_data.pop(key)
                self.cache_data[key] = item
            else:
                discard = self.cache_data.popitem()
                print(f'DISCARD: {discard[0]}')
        self.cache_data[key] = item
        return self.cache_data

    def get(self, key):
        '''gets item from dictionary'''
        if key is not None or key in self.cache_data:
            return self.cache_data[key]
        return None
