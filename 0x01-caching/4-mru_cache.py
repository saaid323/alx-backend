#!/usr/bin/env python3
'''implement  MRU Caching'''
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    '''class that inherits from BaseCaching and is a caching system'''

    def __init__(self):
        super().__init__()

    def last_key(self, data):
        '''return the last key'''
        myList = [i for i in self.cache_data.keys()]
        return myList[-1]

    def put(self, key, item):
        '''adds item to the dictionary'''
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            if self.cache_data.get(key) is not None:

                del self.cache_data[key]
                self.cache_data[key] = item
            else:
                last = self.last_key(self.cache_data)
                discard = self.cache_data.pop(self.last_key(self.cache_data))
                print(f'DISCARD: {last}')
        if key is not None or item is not None:
            self.cache_data[key] = item
        self.cache_data[key] = item

        return self.cache_data

    def get(self, key):
        '''gets item from dictionary'''
        if self.cache_data.get(key) is None:
            return None
        item = self.cache_data[key]
        del self.cache_data[key]
        self.cache_data[key] = item
        return self.cache_data[key]
