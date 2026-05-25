#!/usr/bin/python3
"""
Module for using list sorting without affecting the original list
"""


class MyList(list):
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
