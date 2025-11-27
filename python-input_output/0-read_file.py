#!/usr/bin/python3
"""
    Fayli oxuayn kod
"""


def read_file(filename=""):
    """
    Bu funkisya fayli oxuyur
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
