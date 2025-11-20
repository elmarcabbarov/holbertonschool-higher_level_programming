#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_my_list = []
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        for i in range(len(my_list)):
            if i == idx :
                continue
            else:
                new_my_list.append(my_list[i])
    
    my_list = new_my_list
    return my_list
