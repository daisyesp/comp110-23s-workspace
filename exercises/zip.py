"""Challenge Question 04 - Dict Function Writing."""
__author__ = "730566314"


def zip (list_str: list[str], list_int: list[int]) -> dict[str,int]:
    """Given two lists of elements produce a dictionary where the keys are the items of the first list and the values are the corresponding items at the same index of the second list."""
    empty = {}
    if (len(list_str) == 0 or len(list_int) == 0 or (len(list_str)) != len(list_int)):
        return empty
    full = {}
    length = int(len(list_str))
    for x in range(length):
        full[list_str[x]] = list_int [x]
    return full

