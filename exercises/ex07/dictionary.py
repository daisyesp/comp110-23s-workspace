"""Ex07 - Dictionary Functions."""
__author__ = "730566314"


def invert(a_dict: dict[str, str]) -> dict[str, str]:
    """Returns a dictionary of the value and keys inverted."""
    keys: list[str] = []
    values: list[str] = []
    for x in a_dict:
        keys.append(x)
        values.append(a_dict[x])
    inverted: dict[str, str] = {}
    length: int = len(keys)
    for i in range(length):
        inverted[values[i]] = keys[i]
    return inverted


def favorite_color(pair: dict[str, str]) -> str:
    """Returns the most color appeard in the dictionary of pariings of people and their favorite colors."""
    colors: list[str] = []
    for x in pair:
        colors.append(pair[x])
    popular: int = 0
    for i in range(len(colors)):
        count: int = 1
        for y in range(i + 1, len(colors)):
            if colors[i] == colors[y]:
                count = count + 1
        if count > popular:
            popular = count
            majority = colors[i]
    return majority 


def count(a_list: list[str]) -> dict[str, int]:
    """Counts the number of vaules in a given list."""
    new: dict[str, int] = {}
    for x in a_list:
        if (x in new):
            new[x] += 1
        else:
            new[x] = 1
    return new