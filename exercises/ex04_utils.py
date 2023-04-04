"""Ex04 - 'list' Utility Functions."""
__author__ = "730566314"


def all(order: list[int], input_int: int) -> bool:
    """Returns True if inputed integer is equal to all integers in list, otherwise False."""
    start = 0
    i = 0
    if (len(order)) == 0:
        return False
    else:
        while (i < len(order)):
            if (input_int == order[start]):
                start = start + 1  
            i += 1
        if (start == len(order)):  
            return True
        else:
            return False


def max(order: list[int]) -> int:
    """Returns the maximum number from list of integers."""
    max = order[0]
    i = 0
    if (len(order) == 0):
        raise ValueError("max() arg is an empty List")
    while i < len(order):
        if max < order[i]:
            max = order[i]
        i += 1
    return max


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Returns True if every element at every index is equal in both lists."""
    index = 0
    track = 0
    if (len(list_one) == len(list_two)):
        while index < len(list_one):
            if (list_one[index] == list_two[index]):
                track += 1
            index += 1
        if track == len(list_one):
            return True
        else:
            return False
    else:
        return False