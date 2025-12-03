#!/usr/bin/python3
"""Import sys ve urllib"""
import urllib.request
import sys

"""Yoxlanish"""
if len(sys.argv) < 2:
    print()
else:
    with urllib.request.urlopen(sys.argv[1]) as r:
        """Hell"""
        print(req.getheader("X-Request-Id"))
