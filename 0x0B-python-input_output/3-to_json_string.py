#!/usr/bin/python3
import json

""" defines a function that creates a string JSON object file """


def to_json_string(my_obj):
    """ change a python obj to a JSON object string file """
    return json.loads(my_obj)
