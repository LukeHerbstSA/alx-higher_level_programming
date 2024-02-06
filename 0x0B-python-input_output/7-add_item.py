#!/usr/bin/python3
"""
pedantic pedantic pedantic documentation
"""
from save_to_json_file.py import save_to_json_file
from load_from_json_file import 6-load_from_json_file.py
import sys
import json

mylist = []

for i in range(1, len(sys.argv)):
    mylist.append(sys.argv[i])
mylist = json.dumps(mylist)
with open("add_item.json", "w+", encoding="utf-8") as myfile:
    myfile.write(mylist)
