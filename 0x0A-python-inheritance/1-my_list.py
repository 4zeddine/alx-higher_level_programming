#!/usr/bin/python3
"""Defines a subclass of list"""


class MyList(list):
    """subclass of list"""
    def __init__(self):
        """initializes the instance"""
        super().__init__()

    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
