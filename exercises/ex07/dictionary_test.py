"""Unit tests for ex07."""

from dictionary import invert, favorite_color, count
import pytest


def test_invert_empty() -> None:
    """Returns empty dictionry given empty dictionary."""
    a_dict: dict[str, str] = {}
    assert invert(a_dict) == {}


def test_error() -> None:
    """Returns keyerror if repeaed values exist."""
    with pytest.raises(KeyError):
        a_dict: dict[str, str] = {'kris': 'jordan', 'michael': 'jordan'}
        invert(a_dict)


def test_invert_letters() -> None:
    """Tests a dictionary with multiple values."""
    a_dict: dict[str, str] = {'a': 'b', 'c': 'd', 'e': 'f'}
    assert invert(a_dict) == {'b': 'a', 'd': 'c', 'f': 'e'}


def test_favorite_color_empty() -> None:
    """Tests a dictionary with empty values."""
    pair: dict[str, str] = {}
    assert favorite_color(pair)


def test_favorite_color_one() -> None:
    """Tests a dictionary with one value."""
    pair: dict[str, str] = {'Daisy': 'green'}
    assert favorite_color(pair) == 'green'


def test_favorite_color_many() -> None:
    """Tests a dictionary with multiple values."""
    pair: dict[str, str] = {'Toby': 'blue', 'Sam': 'red', 'Ethan': 'blue'}
    assert favorite_color(pair) == 'blue'


def test_count_one() -> None:
    """Tests an empty list."""
    a_list: list[str] = ['1']
    assert count(a_list) == {'1': 1}


def test_count_empty() -> None:
    """Tests a list with one value."""
    a_list: list[str] = []
    assert count(a_list) == {}


def test_count_many() -> None:
    """Tests a list wiht multiple values."""
    a_list: list[str] = ['1', '3', '3', '2', '1', '1']
    assert count(a_list) == {'1': 3, '3': 2, '2': 1}