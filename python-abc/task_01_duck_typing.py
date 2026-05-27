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
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """ This is a circle
        it knows how to get around
        its got a radius from centre to rim
        """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)

    def perimeter(self):
        return pi * 2 * self.radius


class Rectangle(Shape):
    """ I am rectangular
        """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width * 2) + (self.height * 2)


def shape_info(shape):
    """ If it talks and walks like a shape,
        its a shape
        """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
