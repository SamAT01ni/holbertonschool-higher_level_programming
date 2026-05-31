#!/usr/bin/python3
"""
Flying fish are very tasty
I had some in barbados
"""


class Fish:
    """ Class is fish, and fish are class"""
    def swim(self):
        print("The fish is swimming")
    def habitat(self)
        print("The fish lives in the water")

class Bird:
    """Emus are flightless birds, so they do not fit this class"""
    def fly(self):
        print("The bird is flying")
    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """ I mean, flying fish dont really fly or live in the sky"""
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
