#!/usr/bin/python3
"""
Verilenleri Python-a çevirir
"""


import json


def from_json_string(my_str):
    """
    Jsondan Pythona çeviren funksiya
    """
    data = json.loads(my_str)
    return data
