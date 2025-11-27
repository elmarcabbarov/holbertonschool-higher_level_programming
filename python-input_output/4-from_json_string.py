#!/usr/bin/python3
"""
Verilenleri Python-a çevirir
"""


import json


def to_json_string(my_obj):
    """
    Jsondan Pythona çeviren funksiya
    """
    data = json.loads(my_obj)
    return data
