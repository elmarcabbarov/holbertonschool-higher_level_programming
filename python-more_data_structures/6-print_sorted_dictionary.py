#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    result = ''
    for k, v in sorted(a_dictionary.items()):
        result += str(k)
        result += ": "
        result += str(v)
        result += '\n'
    return result
