#!/usr/bin/python3
"""Import et"""
import requests as r
import sys

"""Yoxlanish"""
if len(sys.argv) < 3:
    print()
else:
    """Emailin gonderilmesi"""
    url = sys.argv[1]
    mail = sys.argv[2]
    data = {"email": mail}
    req = r.post(url, data=data)
    print(req.text.strip())
