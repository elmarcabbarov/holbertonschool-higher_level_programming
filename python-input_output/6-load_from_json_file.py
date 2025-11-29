#!/usr/bin/python3
"""jsona object cevirmek kimi bir sey"""

import json


def load_from_json_file(filename):
    """indi deserialize elemek ucun load()
    istifade edecik bir de with open bayaqki"""

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
