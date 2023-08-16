#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if ((search > len(my_list) - 1) or search < 0):
        return (my_list)
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return (new_list)
