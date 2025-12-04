#!/usr/bin/python3
"""" URLe reponse atan requests kitabxanasini istifade eden kod"""


import requests as r
import sys

if len(sys.argv) < 2:
    print()
else:
    url = sys.argv[1]
    req = r.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
