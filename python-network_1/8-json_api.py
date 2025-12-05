#!/usr/bin/python3
"""Send POST request to search_user with letter in q variable"""

import requests
import sys

# 1. URL
url = "http://0.0.0.0:5000/search_user"

# 2. q dəyəri
if len(sys.argv) > 1:
    q = sys.argv[1]
else:
    q = ""

# 3. POST sorğusu
response = requests.post(url, data={'q': q})

# 4. JSON emalı
try:
    data = response.json()
    if not data:
        print("No result")
    else:
        print(f"[{data['id']}] {data['name']}")
except ValueError:
    print("Not a valid JSON")
