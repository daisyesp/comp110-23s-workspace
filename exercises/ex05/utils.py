"""Ex05 - 'List' Utility Functions."""
__author__ = "730566314"


def only_evens(order: list[int]) -> list[int]: 
    """Return only even numbers from given list."""
    evens_list = []
    for idx in order:
        if idx % 2 == 0:
            evens_list.append(idx)
    return evens_list


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Given two lists, generate new list of containing all the first elements, followed by second elements, etc."""
    new_list = []
    for num in list_1:
        new_list.append(num)
    for num in list_2:
        new_list.append(num)
    return new_list


def sub(alist: list[int], start: int, end: int) -> list[int]:
    """A List which is a subset of the given list, between the specified start index and the end index - 1."""
    if start < 0:
        start = 0
    if end > len(alist):
        end = len(alist)
    if start >= end or len(alist) == 0 or start >= len(alist) or end <= 0:
        return []
    subset = []
    for i in range(start, end):
        subset.append(alist[i])
    return subset
