#!/usr/bin/python3
"""Defines a function that write JSON to a file"""
import json


def save_to_json_file(my_obj, filename):
    """writes Object to a text file, using a JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
