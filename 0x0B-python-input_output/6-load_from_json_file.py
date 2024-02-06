#!/usr/bin/python3
"""Defines a function that creates an object from JSON"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""
    with open(filename) as f:
        return json.load(f)
