#!/usr/bin/python3
"""import et"""
import requests
"""Melumati elde et ve cap et"""
r = requests.get("https://intranet.hbtn.io/status")
r = r.text

print("Body response:")
print("\t- type: {}".format(type(r)))
print("\t- content: {}".format(r))
