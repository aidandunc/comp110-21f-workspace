"""List utility functions."""

__author__ = "123456789"


# TODO: Implement your functions here.

def all(lst: list[int], integer: int) -> bool:
    """Tests to see if all of the integers in a given list match the given integer."""
    incorrect_counter = 0
    i = 0
    if len(lst) == 0:
        return incorrect_counter == -1
    else:
        while i < len(lst):
            if lst[i] == integer:
                None
            else:
                incorrect_counter += 1
            i += 1
    return incorrect_counter == 0
    

def is_equal(lstt1: list[int], lstt2: list[int]) -> bool:
    """Tests to see if two lists are equal."""
    i = 0
    if len(lstt1) != len(lstt2):
        return False
    elif len(lstt1) and len(lstt2) == 0:
        return True
    else:
        while i < len(lstt1):
            if lstt1[i] == lstt2[i]:
                None
            else:
                return False
            i += 1
        return True


is_equal([], [1])


def max(lsst1: list[int]) -> int:
    """Finds the element with the maximum value in a list of integers."""
    if len(lsst1) == 0:
        raise ValueError("Error: the max argument input was empty.")
        return None
    else:
        i = 1
        current_max = lsst1[0]
        while i < len(lsst1):
            if current_max > lsst1[i]:
                None
            else:
                current_max = lsst1[i]
            i += 1
        return current_max


max([0, -2, -5, -6])
