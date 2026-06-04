#!/usr/bin/python3
""" Serial, not cereal
I want crunchy nut
"""


import json


def serialize_and_save_to_file(data, filename):
    """ Serialise and save """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """ Load and deserialise """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
