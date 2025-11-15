#!/usr/bin/python3
def uppercase(str):
    """
    Prints a string in uppercase followed by a new line.

    Args:
        str: A string to convert to uppercase
    """
    for i in range(len(str)):
        if ord('a') <= ord(str[i]) <= ord('z'):
            print("{:c}".format(ord(str[i]) - 32), end="")
        else:
            print("{:c}".format(ord(str[i])), end="")
    print()
