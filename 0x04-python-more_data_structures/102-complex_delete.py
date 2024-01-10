#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    to_del = []
    for key, val in a_dictionary.items():
        if val == value:
            to_del.append(key)
    for key in to_del:
        del a_dictionary[key]
    return a_dictionary
