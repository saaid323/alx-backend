#!/usr/bin/env python3
'''Implements first in fiirst out'''
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''class that inherits from BaseCaching and is a caching system'''

    def __init__(self):
        '''Initiliaze the class'''
        super().__init__()

    def first_key(self, data):
        '''return the first key'''
        myList = [i for i in self.cache_data.keys()]
        return myList[0]

    def put(self, key, item):
        '''puts items into the dictionary'''
        if key is None or item is None:
            return
        if key is not None or item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if self.cache_data.get(key) is not None:
                    self.cache_data.pop(key)
                    self.cache_data[key] = item
                else:
                    discarded = self.first_key(self.cache_data)
                    del self.cache_data[self.first_key(self.cache_data)]
                    print(f'DISCARD: {discarded}')

            self.cache_data[key] = item
            return self.cache_data

    def get(self, key):
        '''return the item in the dictionary'''
        if key is None or self.cache_data[key] is None:
            return None
        return self.cache_data[key]
