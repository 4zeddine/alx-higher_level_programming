#!/usr/bin/python3
"""Defines a rebel class MyInt that inherits from int."""


class MyInt(int):
    """inverts the == and != operators."""

    def __eq__(self, value):
        """change == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """change != operator with == behavior."""
        return self.real == value
