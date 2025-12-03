#!/usr/bin/python3
"""Sends a POST request with an email to the given URL."""


import requests as r
import sys

"""Yoxlanish"""
if len(sys.argv) < 3:
    print()
else:
    """Emailin gonderilmesi"""
    url = sys.argv[1]
    mail = sys.argv[2]
    e = {"email": mail}
    req = r.post(url, data=e)
    print(req.text.strip())
