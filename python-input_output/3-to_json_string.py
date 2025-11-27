#!/usr/bin/python3
"""
Verilenleri JSON-a çevirir
"""


import json


def to_json_string(my_obj):
    """
    Jsona çeviren funksiya
    """
    json_string = json.dumps(my_obj, ensure_ascii=False, indent=2)
    xreturn json_string
