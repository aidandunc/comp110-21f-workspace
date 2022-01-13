"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730530326"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_half() -> None:
    """Tests only_evens function for list with half even numbers."""
    evens: list[int] = [1, 2, 3, 4]
    assert only_evens(evens) == [2, 4]


def test_only_evens_most() -> None:
    """Tests only_evens function for list with mostly even numbers."""
    evens: list[int] = [4, 6, 8, 7, 10]
    assert only_evens(evens) == [4, 6, 8, 10]


def test_only_evens_none() -> None:
    """Tests only_evens function for list with no even numbers."""
    evens: list[int] = [1, 1, 3, 5, 7]
    assert only_evens(evens) == []


def test_sub_front_to_back() -> None:
    """Tests sub function for small list with start index at the beginning of list and end index at the end of it (and larger than the number of the last index in list to test exclusivity of end index)."""
    total_list: list[int] = [1, 2, 3, 4]
    start_index = 0
    end_index = 4
    assert sub(total_list, start_index, end_index) == [1, 2, 3, 4]


def test_sub_use_small_subset() -> None:
    """Tests sub function for small list with start index in middle of list and end index at end (and larger than the number of the last index in list to test exclusivity of end index)."""
    total_list: list[int] = [2, 34, 2, 21, 27]
    start_index = 2
    end_index = 5
    assert sub(total_list, start_index, end_index) == [2, 21, 27]
    

def test_sub_empty_list() -> None:
    """Tests sub function for empty list."""
    total_list: list[int] = []
    start_index = 3
    end_index = 8
    assert sub(total_list, start_index, end_index) == []


def test_concat_use() -> None:
    """Tests concat function with two lists that are the same."""
    list1: list[int] = [1, 2, 3, 4]
    list2: list[int] = [1, 2, 3, 4]
    assert concat(list1, list2) == [1, 2, 3, 4, 1, 2, 3, 4]


def test_concat_use_two() -> None:
    """Tests concat function with two different lists of different sizes."""
    list1: list[int] = [10, 20, 35, 43]
    list2: list[int] = [13, 2, 506]
    assert concat(list1, list2) == [10, 20, 35, 43, 13, 2, 506]


def test_concat_edge() -> None:
    """Tests concat function with two empty lists."""
    list1: list[int] = []
    list2: list[int] = []
    assert concat(list1, list2) == []