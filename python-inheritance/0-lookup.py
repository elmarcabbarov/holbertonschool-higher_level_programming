#!/usr/bin/python3
"""
obyektleri bilmem ne bilmem ne eden kod
"""


def lookup(obj):
    """
    obyektleri qaytarir list kimi
    """
    return list(dir(obj))
