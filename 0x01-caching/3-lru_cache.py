#!/usr/bin/env python3
'''implements LRU Caching'''
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''class that inherits from BaseCaching and is a caching system'''

    def __init__(self):
        super().__init__()

    def first_key(self, data):
        '''return the first key'''
        myList = [i for i in self.cache_data.keys()]
        return myList[0]

    def put(self, key, item):
        '''puts items in a dictionary'''
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            if self.cache_data.get(key) is not None:
                del self.cache_data[key]
                self.cache_data[key] = item
            else:
                first = self.first_key(self.cache_data)
                discard = self.cache_data.pop(self.first_key(self.cache_data))
                print(f'DISCARD: {first}')
        self.cache_data[key] = item

    def get(self, key):
        '''gets item from dictionary'''
        if self.cache_data.get(key) is None:
            return None
        item = self.cache_data[key]
        del self.cache_data[key]
        self.cache_data[key] = item
        return self.cache_data.get(key)
