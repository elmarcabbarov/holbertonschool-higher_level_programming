#!/usr/bin/python3
"""
    Fayli append eleyir
"""


def append_write(filename="", text=""):
    """
    Bu funkisya fayli append edir
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
