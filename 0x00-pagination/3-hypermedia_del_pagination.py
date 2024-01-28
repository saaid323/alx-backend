#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        '''return dictionary with the following key-value pairs'''
        assert index < len(self.__indexed_dataset)
        all_names = []
        next_index = index + page_size
        start = index
        finish = next_index
        while start < finish:
            if self.indexed_dataset().get(start) is None:
                finish += 1
                start += 1
                continue
            all_names.append(self.indexed_dataset().get(start))
            start += 1
        dic = {
            'index': index,
            'data': all_names,
            'page_size': page_size,
            'next_index': next_index}
        return dic
