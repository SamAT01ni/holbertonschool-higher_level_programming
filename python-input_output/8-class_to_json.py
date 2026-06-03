#!/usr/bin/python3
""" Hello. Today we get dict description with some json serielisation or something """


import json


def class_to_json(obj):
    """ Makes attributes of obj class serialisable """
    return obj.__dict__
