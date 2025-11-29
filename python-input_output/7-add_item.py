#!/usr/bin/python3
"""verilenleri  python liste ordan da filea"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
filename = "add_item.json"

"""Eger fayl yoxdusa yart"""

try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

"""Burda da clide verilen elemnetleri liste daxil edir"""

my_list.extend(sys.argv[1:])

"""Filei yeniden yadda saxlayir"""

save_to_json_file(my_list, filename)
