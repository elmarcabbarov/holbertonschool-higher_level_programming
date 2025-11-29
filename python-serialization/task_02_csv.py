#!/usr/bin/python3
"""
CSV den JSONA
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """ CSVnin oxunmasi"""
    try:
        with open(csv_filename, "r", encoding="utf-8") as f:
            csv_reader = csv.DictReader(f)
            data = []
            for row in csv_reader:
                data.append(row)

        """CSVnin jsona elave edilmesi"""
        with open("data.json", "w", encoding="utf-8") as j:
            json.dump(data, j)
        return True

        """Eks halda False qyatarir"""
    except BaseException:
        return False
