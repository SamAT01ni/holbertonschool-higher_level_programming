#!/usr/bin/python3
"""
"Print Square" module
Prints a square of #
Enter a number that is the square
"""


def print_square(size):
    """Print a square
    I have given up on life
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
