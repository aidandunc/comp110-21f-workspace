"""Example of writing a test subject."""


def sum(xs: list[float]) -> float:
    """Compute the sum of a list of floats."""
    total: float = 0.0
    i: int = 0
    while i < len(xs):
        total += xs[i]
        i += 1
    return total