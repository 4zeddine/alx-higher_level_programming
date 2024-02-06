#!/usr/bin/python3
"""Defines a function that reads files text."""


def read_file(filename=""):
    """prints the content of a UTF8 text file to stdout."""
    with open(filename, encoding="UTF-8") as f:
        print(f.read(), end="")
