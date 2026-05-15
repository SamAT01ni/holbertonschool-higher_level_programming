#!/usr/bin/python3
"""
"Add integer" module
Adds integers or floats together.
Floats become ints
"""


def add_integer(a, b=98):
    """Returns the sum of floats and integers as an integer
    TypeError is raised if not correct type
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
