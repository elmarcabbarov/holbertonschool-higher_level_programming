#!/usr/bin/python3
"""Post gondermek requests kitabxanasi ile"""


import requests as r, sys

if len(sys.argv) < 1:
    q =""
else:
    
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1]
    data = {"q": q}
    res = r.post(url, data=data)
    try:
        data = r.json()
    except ValueError:
        print("Not a valid JSON")
    if not data:
        print("No result")
    else:
        print(f"{data["id"]} {data["name"]}")

