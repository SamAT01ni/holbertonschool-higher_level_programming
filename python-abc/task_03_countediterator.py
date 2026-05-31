#!/usr/bin/python3
"""
Welcome to my script
Iterative module
"""

class CountedIterator:
    """ Counted iterator wowaweewa """
    def __init__(self, iterable):
        self.iter = iter(iterable)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.iter)
        self.count += 1
        return item

    def get_count(self):
        return self.count
