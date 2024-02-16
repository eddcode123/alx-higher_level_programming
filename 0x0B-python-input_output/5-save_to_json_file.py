#!/usr/bin/python3

""" defines a function that writes an object in json form to a file """
import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.loads(my_obj))
