#!/usr/bin/python3
"""Defines inherit list class MyList."""


class MyList(list):
    """Implements sorted print for built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
