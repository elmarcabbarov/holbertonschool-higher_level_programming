#!/usr/bin/python3
"""Kitabxanini import et"""
import urllib.request

"""URLle isler """
with urlib.request.urlopen("https://intranet.hbtn.io/status") as response:
    data = response.read()
    """Print et"""
    print("Body response:")
    print("\t- type: {}".format(type(body))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode("utf-8")))
