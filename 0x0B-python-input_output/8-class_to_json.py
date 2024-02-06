#!/usr/bin/python3
"""Defines function that returns dictionary description"""


def class_to_json(obj):
    """Return the dictionary represntation with simple data structure."""
    return obj.__dict__
