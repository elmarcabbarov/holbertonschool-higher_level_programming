#!/usr/bin/python3
"""Kitabxanini import et"""
import urllib.request

"""URLle isler """
with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
    data = response.read()
"""Print et"""
print("Body response:")
print("\t- type: {}".format(type(data)))
print("\t- content: {}".format(data))
print("\t- utf8 content: {}".format(data.decode("utf-8")))
