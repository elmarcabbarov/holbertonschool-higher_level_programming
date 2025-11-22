#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for key, value in a_dictionary.items():
        v = value * 2
        a_dictionary[key] = v
    return a_dictionary
