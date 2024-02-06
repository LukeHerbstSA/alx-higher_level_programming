#!/usr/bin/python3
"""
pedantic pedantic pedantic documentation
"""
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file
import sys
import json

mylist = []

for i in range(1, len(sys.argv)):
    mylist.append(sys.argv[i])
with open("add_item.json", "w+", encoding="utf-8") as myfile:
    json.dump(mylist, myfile)
