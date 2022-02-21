"""Utils document for Exercise 5."""

__author__ = "730484959"


def only_evens(list_of_ints: list[int]) -> list[int]:
    """Given a list of integers, it returns only the even integers in the list."""
    i: int = 0
    while i < len(list_of_ints):
        if list_of_ints[i] % 2 != 0:
            list_of_ints.pop(i)
        else:
            i += 1
    return list_of_ints


def sub(list_of_ints: list[int], start: int, end: int) -> list[int]:
    """Given a list of integers and a start and end index, it generates a list which is a subset of the given list between the two indices."""
    i: int = start
    new_list: list[int] = []
    if start < 0:
        i = 0
    if end > len(list_of_ints):
        end = len(list_of_ints)
    if len(list_of_ints) == 0 or start > len(list_of_ints) or end <= 0:
        return new_list
    while i < len(list_of_ints) and i < end:
        new_list.append(list_of_ints[i])
        i += 1
    return new_list


def concat(first_list_of_ints: list[int], second_list_of_ints: list[int]) -> list[int]:
    """Given two lists of integers, it generates a list containing all of the elements of the first list followed by all of the elements of the second list."""
    i: int = 0
    new_list: list[int] = []
    while i < len(first_list_of_ints):
        new_list.append(first_list_of_ints[i])
        i += 1
    i = 0
    while i < len(second_list_of_ints):
        new_list.append(second_list_of_ints[i])
        i += 1
    return new_list
