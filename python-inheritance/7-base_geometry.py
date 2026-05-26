#!/usr/bin/python3
"""
Base Geometry module
Who knows what we'll get up to here
"""


class BaseGeometry:
    """ Base geometry
        i gotta have this or betty will neuter me
        """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
