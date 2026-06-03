#!/usr/bin/python3
""" append write module """


def append_write(filename="", text=""):
    """ appends string at end of a text file """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
