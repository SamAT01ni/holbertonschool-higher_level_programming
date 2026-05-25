#!/usr/bin/python3
"""
Module for using list sorting without affecting the original list
Nothing ever happens
"""


class MyList(list):
    """ MyList module is my list.
        And noone
        Can take it away"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
