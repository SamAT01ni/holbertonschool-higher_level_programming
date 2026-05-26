#!/usr/bin/python3
"""
Back to squares woo
Module
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Squares have returned. Back home we have crisps called squares.
        I miss them
        """

    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return (f"[Square] {self.__size}/{self.__size}")
