#!/usr/bin/python3
"""Import etdik"""
import urllib.request
import sys

"""Validation"""

if len(sys.argv) < 2:
    print()
else:
    url = sys.argv[1]
"""Try except"""
   try:
        with urllib.request.urlopen(url) as r:
            print(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
