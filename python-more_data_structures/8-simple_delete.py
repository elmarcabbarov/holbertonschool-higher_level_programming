#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = {}
    for key, value in a_dictionary.items():
        v = value * 2
        b_dictionary[key] = v
    return b_dictionary, a_dictionary
