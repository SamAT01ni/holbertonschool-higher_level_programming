#!/usr/bin/python3
"""
got to inheritance now woo
returns true if inherited
"""


def inherits_from(obj, a_class):
    """Checks if object tha tinherited from the class"""
    if (type(obj) is not a_class):
        return issubclass(type(obj), a_class)
    else:
        return False
