#!/usr/bin/python3
"""
    Fayli oxuayn kod
"""


def write_file(filename="", text=""):
    """
    Bu funkisya fayli oxuyur
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
