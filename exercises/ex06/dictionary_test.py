"""Tests for dictionary.py for Exercise 6."""

__author__ = "730484959"

from dictionary import invert, favorite_color, count


def test_invert_empty() -> None:
    """Given an empty dictionary, it returns an empty dictionary."""
    string_dictionary: dict[str, str] = {}
    assert invert(string_dictionary) == {}


def test_invert_one_key() -> None:
    """Given a dictionary with only one key-value pair, it returns one key-value pair."""
    string_dictionary: dict[str, str] = {"Nathan": "Kelete"}
    assert invert(string_dictionary) == {"Kelete": "Nathan"}


def test_invert_standard() -> None:
    """Given a dictionary with x strings, it returns x key-value pairs."""
    string_dictionary: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(string_dictionary) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_favorite_color_empty() -> None:
    """Given an empty dictionary, it returns an empty."""
    string_dictionary: dict[str, str] = {}
    assert favorite_color(string_dictionary) == ""


def test_favorite_color_tie() -> None:
    """Two."""
    string_dictionary: dict[str, str] = {"Nathan": "purple", "Ahmad": "lavender"}
    assert favorite_color(string_dictionary) == "purple"


def test_favorite_color_multiple() -> None:
    """Many."""
    string_dictionary: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(string_dictionary) == "blue" 


def test_count_empty() -> None:
    """Empty."""
    input_string: list[str] = []
    assert count(input_string) == {}


def test_count_one() -> None:
    """One."""
    input_string: list[str] = ["Nathan"]
    assert count(input_string) == {"Nathan": 1}


def test_count_many() -> None:
    """Many."""
    input_string: list[str] = ["Nathan", "Nathan", "Nathan"]
    assert count(input_string) == {"Nathan": 3}