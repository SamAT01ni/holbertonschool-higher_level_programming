#!/usr/bin/python3
from abc import ABC, abstractmethod
"""
This is an abstract class module
with animals and other 4 legged things
"""


class Animal(ABC):
    """Abstrast claas otherwise known as animal
        """
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """Subclass of dog
        """
    def sound(self):
        return ("Bark")

class Cat(Animal):
    """ Subclass of cat
        """
    def sound(self):
        return ("Meow")
