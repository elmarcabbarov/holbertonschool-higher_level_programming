#!/usr/bin/python3
def no_c(my_string):
    my_list = list(my_string)
    result = ""
    for i in my_list:
        if i !="c" and i != "C":
           result = result + i
    return result
