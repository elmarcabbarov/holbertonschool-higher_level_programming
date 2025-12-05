#!/usr/bin/python3
"""Post gondermek requests kitabxanasi ile"""


import requests as r
import sys

if len(sys.argv) < 1:
    q = ""
else:
    q = sys.argv[1]

url = "http://0.0.0.0:5000/search_user"
data = {"q": q}
req = r.post(url, data=data)

try:
    if not data:
        print("No result")
    else:
        print(f"{data['id']} {data['name']}")
except ValueError:
    print("Not a valid JSON")
