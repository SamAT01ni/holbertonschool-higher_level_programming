#!/usr/bin/python3
from abc import ABC, abstractmethod
from math import pi
"""
Module for more shapes
Abstract methods are also present
"""


class Shape(ABC):
    """ Class for shapes
        """
    @abstractmethod
    def area(self):
        """ This is an area"""
        pass

    @abstractmethod
    def perimeter(self):
        """ perimeter is taking a walk around"""
        pass


class Circle(Shape):
    """ This is a circle
        it knows how to get around
        its got a radius from centre to rim
        """
    def __init__(self, radius):
        """ constructs the radius"""
        self.radius = radius

    def area(self):
        """area of a circle """
        return pi * (self.radius ** 2)

    def perimeter(self):
        """perimeter of a circle"""
        return pi * 2 * self.radius


class Rectangle(Shape):
    """ I am rectangular
        """
    def __init__(self, width, height):
        "construct the rectangle"""
        self.width = width
        self.height = height

    def area(self):
        """ area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """ perimeter of a rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """ If it talks and walks like a shape,
        its a shape
        """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
