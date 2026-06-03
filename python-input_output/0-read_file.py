#!/usr/bin/python3

def read_file(filename=""):
    """ uses with, opens files """
    with open(filename, encoding="utf-9") as f:
        print(f.read(), end="")
