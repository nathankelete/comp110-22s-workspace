"""Utils test document for Exercise 5."""

__author__ = "730484959"

from utils import only_evens 
from utils import sub
from utils import concat


def test_only_evens_empty() -> None:
    """Given an empty list of integers, it returns an empty list."""
    list_of_ints: list[int] = []
    assert only_evens(list_of_ints) == []


def test_only_evens_one_odd() -> None:
    """Given a list of integers containing 1 odd number, it returns only the even integers in the list."""
    list_of_ints: list[int] = [1, 2, 3]
    assert only_evens(list_of_ints) == [2]
    

def test_only_evens_two_odds() -> None:
    """Given a list of integerscontaing 2 odd numbers, it returns only the even integers in the list."""
    list_of_ints: list[int] = [1, 5, 3]
    assert only_evens(list_of_ints) == []


def test_sub_empty() -> None:
    """Given an empty list of integers, it returns an empty list."""
    list_of_ints: list[int] = []
    assert sub(list_of_ints, 1, 3) == []


def test_sub_four_ints() -> None:
    """Given a list of four integers, it returns a list with only the integers between the start and end index."""
    list_of_ints: list[int] = [10, 20, 30, 40]
    assert sub(list_of_ints, 1, 3) == [20, 30]


def test_sub_negative_start() -> None: 
    """Given a list of four integers, it returns a list with only the integers between the start and end index."""
    list_of_ints: list[int] = [10, 20, 30, 40]
    assert sub(list_of_ints, -5, 9) == [10, 20, 30, 40]


def test_concat_empty() -> None:
    """Given an empty list of integers, it returns an empty list."""
    first_list_of_ints: list[int] = []
    second_list_of_ints: list[int] = []
    assert concat(first_list_of_ints, second_list_of_ints) == []


def test_concat_one_ints() -> None:
    """Given two lists of integers, it generates a list containing all of the elements of the first list followed by all of the elements of the second list."""
    first_list_of_ints: list[int] = [1]
    second_list_of_ints: list[int] = [2]
    assert concat(first_list_of_ints, second_list_of_ints) == [1, 2]


def test_concat_two_ints() -> None:
    """Given two lists of integers, it generates a list containing all of the elements of the first list followed by all of the elements of the second list."""
    first_list_of_ints: list[int] = [1, 2]
    second_list_of_ints: list[int] = [3, 4]
    assert concat(first_list_of_ints, second_list_of_ints) == [1, 2, 3, 4]