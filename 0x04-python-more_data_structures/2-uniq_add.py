#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list (only once for each integer)"""
    list_to_set = set(my_list)
    return sum(list_to_set)
