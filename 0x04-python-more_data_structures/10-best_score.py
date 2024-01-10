#!/usr/bin/python3
def best_score(a_dictionary):
    """Function that returns a key with the biggest integer value"""

    if a_dictionary is None:
        return None

    if len(a_dictionary) == 0:
        return None

    values_list = list(a_dictionary.values())
    max_value = max(values_list)
    for key, value in a_dictionary.items():
        if value == max_value:
            return key
