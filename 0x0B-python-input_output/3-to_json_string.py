#!/usr/bin/python3
"""Defines a string-to-JSON function code."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a string object code."""
    return json.dumps(my_obj)
