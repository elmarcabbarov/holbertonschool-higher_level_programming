#!/usr/bin/python3

"""Post gondermek requests kitabxanasi ile"""


import requests as r

import sys


if len(sys.argv) > 1:
    q = sys.argv[1]
else:
    q = ""

url = "http://0.0.0.0:5000/search_user"

nermin = {"q": q}

try:
    req = r.post(url, data=nermin, headers={'cfclearance': 'true'})
    data = req.json()
    if not data:
        print("No result")
    else:
        print(f"[{data['id']}] {data['name']}")
except ValueError:
    print("Not a valid JSON")
