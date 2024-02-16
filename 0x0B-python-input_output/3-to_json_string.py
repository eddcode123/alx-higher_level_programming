#!/usr/bin/python3

""" defines a function that creates a string JSON object file """
import json


def to_json_string(my_obj):
    """ change a python obj to a JSON object string file """
    return json.dumps(my_obj)
