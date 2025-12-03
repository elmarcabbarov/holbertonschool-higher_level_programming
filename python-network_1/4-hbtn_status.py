#!/usr/bin/python3
"""import et"""
import requests
"""Melumati elde et ve cap et"""
r = requests.get("https://intranet.hbtn.io/status")
r = r.text
print("\t- type: {}".format(type(r)))
print("\t- type: {}".format(r))
