#!/usr/bin/python3
def uppercase(str):
    """
    Prints a string in uppercase followed by a new line.

    Args:
        str: A string to convert to uppercase
    """
    result = ""
    for i in range(len(str)):
        if ord('a') <= ord(str[i]) <= ord('z'):
            result += "{:c}".format(ord(str[i]) - 32)
        else:
            result += "{:c}".format(ord(str[i]))
    print("{:s}".format(result))
