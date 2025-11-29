#!/usr/bin/python3
"""
XML serelasiya ve deserelasiya
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serelasiya"""
    try:
        root = ET.Element("data")
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

        return True
    except BaseException:
        return False


def deserialize_from_xml(filename):
    """Deserelasiya XMLden dicte"""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        data = {}

        for elem in root:
            data[elem.tag] = elem.text

        return data

    except BaseException:
        return None
