#!/usr/bin/python3
import sys

save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# create a list of arguments excluding script name
arguments = sys.argv

# if arguments is 1 then make arguments a empty list
if len(arguments) == 1:
    arguments = []
else:
    # make arguments a list of arguments passed
    arguments = sys.argv[1:]

# save list of arguments to a json file
save_to_json(arguments, 'add_item.json')

# load the saved json files to python object
load_from_json_file('add_item.json')
