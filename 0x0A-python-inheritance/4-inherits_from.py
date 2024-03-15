#!/usr/bin/python3
"""Defines inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is inherited instance of the class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match type of obj to.
    Returns:
        If obj is inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
