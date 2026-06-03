#!/usr/bin/python3
""" Create object from json file """


import json


def load_from_json_file(filename):
    """ loading from json file yay"""
    with open(filename) as f:
        return json.load(f)
