#!/usr/bin/python3
"""
I am in Holberton today discussing the topic of squares
Squares a 4 sided quadrilateral with equal sides and 90 degree angles
"""


class Square:
    """It goes in the square hole"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) is not 2 or \
                not all([type(i) is int for i in value]) or \
                not all([i >= 0 for i in value]):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
