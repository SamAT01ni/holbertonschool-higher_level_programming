#!/usr/bin/python3
"""
Module for more shapes
Abstract methods are also present,

We have circles and rectangles and also a lovely shape info fucntion
isnt that splendid
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """ Class for shapes
        get them initialied
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
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """perimeter of a circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """ I am rectangular
        and noone can take it away
        """
    def __init__(self, width, height):
        """construct the rectangle"""
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

