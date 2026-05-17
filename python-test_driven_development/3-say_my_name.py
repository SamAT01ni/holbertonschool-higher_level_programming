#!/usr/bin/python3
"""
"Say My Name" module
Say my name says my name
first and second wow how cool
"""


def say_my_name(first_name, last_name=""):
    """Prints (first) (last)
    or prints error
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
