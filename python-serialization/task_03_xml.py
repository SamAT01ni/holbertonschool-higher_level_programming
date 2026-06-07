#!/usr/bin/python3
""" Module for this stuff now idk"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """ Serielise xml stuff """
    root = ET.Element("data")
    for key, val in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(val)
    oak = ET.ElementTree(root)
    oak.write(filename)


def deserialize_from_xml(filename):
    """ Now desrriealise some trees"""
    oak = ET.parse(filename)
    root = oak.getroot()
    dictionary = {}

    for child in root:
        dictionary[child.tag] = child.text
    return dictionary
