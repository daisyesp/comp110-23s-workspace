"""Unit testing ex05_utils.py."""
__author__ = "730566314"

from exercises.ex05.utils import only_evens, concat, sub

def only_evens_empty() -> None:
    evens_list: list[float] = []
    assert only_evens(evens_list) == 0

def concat_empty() -> None:
    list_1: list[int] = []
    list_2: list[int] = []
    assert concat() == 0

def sub_empty() -> None:
    alist: list[int] = []
    assert sub(alist) == 0

def only_evens_many() -> None:
    test_list: list[float] = [1.0]
    assert only_evens(test_list) == 1.0

def concat_many() -> None:
    test_list: list[float] = [1.0, 2.0, 3.0]
    assert concat(test_list) == 6.0

def sub_many() -> None:
    test_list: list[float] = [1.0, -2.0, 1.0]
    assert sub(test_list) == 0.0

def only_evens_negatives() -> None:
    test_list: list[float] = [1.0]
    assert only_evens(test_list) == 1.0

def concat_negatives() -> None:
    test_list: list[float] = [1.0, 2.0, 3.0]
    assert concat(test_list) == 6.0

def sub_negatives() -> None:
    test_list: list[float] = [1, -2.0, 1.0]
    assert sub(test_list) == 0.0