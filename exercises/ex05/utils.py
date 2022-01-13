"""List utility functions part 2."""

__author__ = "730530326"


def only_evens(evens: list[int]) -> list[int]:
    """Returns a list of the even integers in a given list of integers."""
    i = 0
    final_evens = []
    while i < len(evens):
        if evens[i] % 2 == 0:
            final_evens.append(evens[i])
        else:
            None
        i += 1
    return final_evens


def sub(total_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Returns a specified subset of a given list."""
    subset = []
    if len(total_list) == 0 or start_index > len(total_list) or end_index <= 0:
        return []
    if start_index < 0:
        start_index = 0
    if end_index > len(total_list):
        end_index = len(total_list)
    counter = start_index
    while counter < end_index:
        subset.append(total_list[counter])
        counter += 1
    return subset


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Concatenates two user-inputted lists."""
    concatenation = []
    i = 0 
    if len(list1) > 0:
        while i < len(list1):
            concatenation.append(list1[i])
            i += 1
    else:
        None
    j = 0
    if len(list2) > 0:
        while j < len(list2):
            concatenation.append(list2[j])
            j += 1
    else:
        None
    return concatenation


    
