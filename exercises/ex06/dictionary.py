"""Exercise 6 - Praciting dictionary functions."""

__author__ = "730484959"


def invert(string_dictionary: dict[str, str]) -> dict[str, str]:
    """Given a dictionary of [str, str], it returns a dict[str, str] that inverts the key and the values."""
    new_dict: dict[str, str] = dict()
    for key in string_dictionary:
        new_dict[string_dictionary[key]] = key
    if len(new_dict) != len(string_dictionary):
        raise KeyError("KeyError!")
    return new_dict


def favorite_color(string_dictionary: dict[str, str]) -> str:
    """Given a dictionary of people's favorite colors, it returns the most popular color."""
    new_dict: dict[str, int] = {}
    for key in string_dictionary:
        if string_dictionary[key] not in new_dict:
            new_dict[string_dictionary[key]] = 1
        else: 
            new_dict[string_dictionary[key]] += 1
    value_list: list[int] = []
    for key in new_dict:
        value_list.append(new_dict[key])
    max_value = max(value_list)
    store_list: list[str] = []
    for key in new_dict:
        if new_dict[key] == max_value:
            store_list.append(key)
    if len(store_list) > 1:
        store_list_1 = store_list[0]
        return store_list_1
    return str(store_list[0])   
            

def count(input_string: list[str]) -> dict[str, int]:
    """Given a list, it returns a dictionary with the frequency of each item in the list."""
    return_dict: dict[str, int] = {}
    for item in input_string:
        if item in return_dict:
            return_dict[item] += 1
        else:
            return_dict[item] = 1
    return return_dict
            