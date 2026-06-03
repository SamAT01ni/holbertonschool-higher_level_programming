#!/usr/bin/python3
""" adds all args to a python list and save"""


import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
f = "add_item.json"
l = []

try:
    l = load_from_json_file(f)
except FileNotFoundError:
    l = []

l.extend(sys.argv[1:])
save_to_json_file(l, f)
