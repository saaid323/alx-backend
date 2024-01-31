#!/usr/bin/env python3
'''Implements Least frequently used caching'''
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    '''class that inherits from BaseCaching and is a caching system
    and implements LFU caching'''
    COUNT = {}

    def __init__(self):
        super().__init__()

    def least_accessed(self, data):
        '''return the first key'''
        keys = []
        values = []
        for k, v in self.COUNT.items():
            values.append(v)
            keys.append(k)
        key = values.index(min(values))
        return keys[key]

    def put(self, key, item):
        '''puts items into the dictionary'''
        if key is None or item is None:
            return
        if key is not None or item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if self.cache_data.get(key) is not None:
                    self.COUNT[key] += 1
                    self.cache_data[key] = item
                    return 
                discarded = self.least_accessed(self.cache_data)
                self.cache_data.pop(self.least_accessed(self.cache_data))
                self.COUNT.pop(discarded)
                print(f'DISCARD: {discarded}')
            self.COUNT[key] = 0
            self.cache_data[key] = item
            return self.cache_data

    def get(self, key):
        '''gets item from dictionary'''
        if self.cache_data.get(key) is None:
            return None
        self.COUNT[key] += 1
        return self.cache_data.get(key)
