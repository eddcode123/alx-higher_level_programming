#!/usr/bin/python3

""" defines a function that creates an obj from a json file """
import json


def load_from_json_file(filename):
    """ open file, read contents and create a object """
    with open(filename, 'r', encoding='utf-8') as f:
        obj = json.load(f.read())
    return obj
