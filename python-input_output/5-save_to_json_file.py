#!/usr/bin/python3
"""
Verilenleri Jsondan text faylina yazir
"""


import json


def save_to_json_file(my_obj, filename):
    """
    text fayilina yazan
    """
    data = json.dumbs(my_obj)
    with open(filename, "w") as f:
        f.write(data)
