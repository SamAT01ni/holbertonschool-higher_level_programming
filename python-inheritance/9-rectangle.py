#!/usr/bin/python3
"""
This is a recctangle module
Getting deja vu yet?
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangles are 4 sided quadrilaterals with equal angles
        and 2 sets of equal sides
        Fascinating
        """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return (f"[Rectangle] {self.__width}/{self.__height}")
