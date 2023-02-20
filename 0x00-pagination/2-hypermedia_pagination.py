#!/usr/bin/env python3
import csv
import math
from typing import List, Tuple


class Server:
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert(isinstance(page, int) and isinstance(page_size, int))
        assert(page > 0 and page_size > 0)
        [start, end] = index_range(page, page_size)
        return self.dataset()[start: end]

    def get_hyper(self, page: int, page_size: int) -> dict:
        dataset_records = self.get_page(page, page_size)

        page_dict = math.ceil(len(self.__dataset) / page_size)

        return {
                'page_size': len(dataset_records),
                'page': page,
                'data': dataset_records,
                'next_page': page + 1 if (page + 1) <= page_dict else None,
                'prev_page': page - 1 if (page - 1) > 0 else None,
                'total_pages': page_dict
                
            }


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
