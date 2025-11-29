#!/usr/bin/python3
"""
Serilasiya ve Deserilasiya eden kod
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Python dict-i JSON faylına yazır.
    Mövcud fayl varsa, əvəz olunur.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(data, f)


def load_and_deserialize(filename):
    """JSON faylından dict oxuyur."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
