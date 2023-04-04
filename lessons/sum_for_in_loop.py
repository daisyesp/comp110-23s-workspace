"""Example function for unit tests."""

def sum(xs: list[float]) -> float:
    """Return sum of all elements in xs"""
    sum_total: float = 0.0
    idx: int = 0
    for item in xs:
        sum_total += xs[idx]
    return sum_total