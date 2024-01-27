#!/usr/bin/env python3
'''return the range of items in a page'''


def index_range(page: int, page_size: int) -> tuple:
    '''function that return the start index and last index of a page'''
    first_index = (page_size * page) - page_size
    last_index = page * page_size
    return (first_index, last_index)
