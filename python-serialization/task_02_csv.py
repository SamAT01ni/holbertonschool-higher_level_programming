#!/usr/bin/python3
""" Module for some shit """


import csv
import json


def convert_csv_to_json(file):
    """THrow shit at a wall and see what sticks"""
    try:
        with open(file, mode="r", encoding="utf-8") as cf:
            data = list(csv.DictReader(cf))

        with open("data.json", mode="w", encoding="utf-8") as jf:
            json.dump(data, jf)

        return True

    except FileNotFoundError:
        return False
