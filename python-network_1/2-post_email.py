#!/usr/bin/python3
"""import et"""
import urllib.request
import urllib.parse
import sys

"""Yoxlanish"""
if len(sys.argv) < 2:
    print()

else:
    """Ne bilim nese"""
    url = sys.argv[1]
    mail = sys.argv[2]
    mail = {"email": mail}
    byte = urllib.parse.urlencode(mail).encode("utf-8")
    with urllib.request.urlopen(url, data=byte) as r:
        body = r.read()
    print(body.decode("utf-8"))
