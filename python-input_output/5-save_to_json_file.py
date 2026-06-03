#!/usr/bin/python3
""" Crash bang wallop what a picture """


import json


def save_to_json_file(my_obj, filename):
    """ i have a friend called jason which is close to json """
    with open(filename, "w") as f:
        json.dump(my_obj, file)
