#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    new_set = set()
    for i in my_list:
        new_set.add(i)
    for s in new_set:
        result += s
    return result
