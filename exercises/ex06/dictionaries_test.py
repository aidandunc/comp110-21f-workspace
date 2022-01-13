from exercises.ex06.dictionaries import invert, favorite_color, count
import pytest
"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730530326"
"""Tests for the sum function."""


def test_invert_regular() -> None:
    """Tests regular dictionary for invert function."""
    input: dict[str, str] = {'Aidan': 'Glynn', 'Emma': 'Jane'}
    assert invert(input) == {'Glynn': 'Aidan', 'Jane': 'Emma'}


def test_invert_empty() -> None:
    """Tests empty dictionary for invert function."""
    input: dict[str, str] = {}
    assert invert(input) == {}


def test_invert_keyerror() -> None:
    """Tests a dictionary that when inverted will bring up KeyError for invert function."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_favorite_colors() -> None:
    """Tests regular input dictionary for favorite_colors function. """
    favorites: dict[str, str] = {'Marc': 'yellow', 'Ezri': 'blue', 'Kris': 'blue'}
    assert favorite_color(favorites) == 'blue'


def test_favorite_colors_tie() -> None:
    """Tests tie scenario for favorite colors function."""
    favorites: dict[str, str] = {'Marc': 'yellow', 'Ezri': 'blue', 'Kris': 'blue', 'Aidan': 'yellow'}
    assert favorite_color(favorites) == 'yellow'


def test_favorite_colors_empty() -> None:
    """Tests epty dictionary for favorite_colors function."""
    favorites: dict[str, str] = {}
    assert favorite_color(favorites) == ''


def test_count_regular() -> None:
    """Tests regular list for count function."""
    input: list[str] = ['hi', 'hi', 'hi', 'hi', 'hello', 'hello', 'bye', 'goodbye', 'goodbye', 'goodbye']
    assert count(input) == {'hi': 4, 'hello': 2, 'bye': 1, 'goodbye': 3}


def test_count_one() -> None:
    """Tests length one list for count function."""
    input: list[str] = ['hi']
    assert count(input) == {'hi': 1}


def test_count_empty() -> None:
    """Tests empty list for count funciton."""
    input: list[str] = []
    assert count(input) == {}