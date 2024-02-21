#!/usr/bin/python3
"""Defines a text file-reading function code."""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout prog."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
