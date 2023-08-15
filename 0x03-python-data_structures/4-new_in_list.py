#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_len = len(my_list)
    temp_list = my_list.copy()
    new_list = my_list.copy()
    if (idx < 0) or (idx > list_len):
        return (temp_list)
    new_list[idx] = element
    return (new_list)
