#!/usr/bin/python3
"""Defines a function that trun string-to-JSON."""
import json


def to_json_string(my_obj):
    """returns the JSON representation of a string object."""
    json.dumps(my_obj)
