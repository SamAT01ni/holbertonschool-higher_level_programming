#!/usr/bin/python3
""" Making a student class """


class Student:
    """ define student claass. I am a student and i am sam """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ return dict """
        if isinstance(attrs, list):
            dict1 = {}
            for key in attrs:
                if key in self.__dict__:
                    dict1[key] = self.__dict__[key]
            return dict1
        return self.__dict__

    def reload_from_json(self, json):
        """ Replace attributes"""
        for key, val in json.items():
            setattr(self, key, val)
