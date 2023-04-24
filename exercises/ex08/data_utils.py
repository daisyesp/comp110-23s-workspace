"""Ex08 - Data Wrangling."""
__author__ = "730566314"

from csv import DictReader

def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first parameter rows of data for each column."""
    new: dict[str, list[str]] = {}
    for column in table:
        main_list: list[str] = []
        for x in range(rows):
            if x < len(table[column]):
                main_list.append(table[column][x])
        new[column] = main_list
    return new


def select(table: dict[str, list[str]], colu: list[str]) -> dict[str, list[str]]:
    """Produces a new column-based table with only a specfic subset of the orginial columns."""
    new: dict[str, list[str]] = {}
    for columns in colu:
        if columns in table:
            new[columns] = table[columns]
    return new


def concat(dict1: dict[str, list[str]], dict2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a new column-based table with two column-based tables combined."""
    new: dict[str, list[str]] = {}
    for key in dict1:
        new[key] = dict1[key]

    for key in dict2: 
        if key in new:
            new[key] += dict2[key]
        else: 
            new[key] = dict2[key]
    return new