#!/usr/bin/env python3
'''return the range of items in a page'''
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    '''function that return the start index and last index of a page'''
    first_index = (page_size * page) - page_size
    last_index = page * page_size
    return (first_index, last_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''return the dataset using page and page_size'''
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        Range = index_range(page, page_size)
        all_names = self.dataset()
        names = []
        for i in range(Range[0], Range[1]):
            try:
                names.append(all_names[i])
            except IndexError:
                return []
        return names

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''returns a dictionary detailing about the pagination like the
        number of remaing pages'''
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        Range = index_range(page, page_size)
        all_names = self.dataset()
        names = []
        total_pages = math.ceil(len(self.dataset()) / page_size)
        dic = {'page_size': 0 if total_pages < page else page_size}
        dic['page'] = page
        
        for i in range(Range[0], Range[1]):
            try:
                names.append(all_names[i])
            except IndexError:
                names = []
        dic['data'] = names
        dic['next_page'] = None if page >= total_pages else page + 1
        dic['prev_page'] = page - 1 if page > 1 else None
        dic['total_pages'] = total_pages
        return dic

