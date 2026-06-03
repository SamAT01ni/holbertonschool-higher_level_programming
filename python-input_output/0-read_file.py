#!/usr/bin/python3
""" Module for reading a file using utf8
what else
"""


def read_file(filename=""):
    """ uses with, opens files """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
