#!/usr/bin/python3
""" add the argv text """
import os
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
le = len(sys.argv)
my_list = []

if os.path.exists('add_item.json') is True:
    my_list = load_from_json_file(filename)
for i in range(1, le):
    my_list.append(sys.argv[i])
save_to_json_file(my_list, filename)
