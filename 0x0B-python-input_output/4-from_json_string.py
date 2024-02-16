#!/usr/bin/python3

""" defines a function that returns a python obj from a json string """
import json


def from_json_string(my_str):
    """ decode json string to python string """
    return json.loads(my_str)
