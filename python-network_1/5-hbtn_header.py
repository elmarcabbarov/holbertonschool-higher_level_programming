#!/usr/bin/python3
"""import et"""
import requests as r
import sys
"""Yoxlanish"""
if len(sys.argv) < 2:
    print()
else:
    """URlden header almaq"""
    url = sys.argv[1]
    req = r.get(url)
    print(req.headers["X-Request-I"])
