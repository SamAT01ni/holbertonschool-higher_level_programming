#!/usr/bin/python3
""" Write file module """


def write_file(filename="", text=""):
    """ Use with and utf-8 """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
