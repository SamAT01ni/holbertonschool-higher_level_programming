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
        self.__radius = radius

    def area(self):
        return pi * (self.__radius ** 2)

    def perimeter(self):
        return pi * 2 * self.__radius

class Rectangle(Shape):
    """ I am rectangular
        """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return (self.__width * 2) + (self.__height * 2)

def shape_info(shape):
    """ If it talks and walks like a shape,
        its a shape
        """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
