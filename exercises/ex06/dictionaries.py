"""Practice with dictionaries."""

__author__ = "123456789"

# Define your functions below


def invert(input: dict[str, str]) -> dict[str, str]:
    """This function inverts the keys and value of a user-inputted dictionary."""
    empty = {}
    keys = []
    values = []

    if len(input) == 0:
        return empty
    
    for i in input:
        keys.append(i)
    for j in input:
        values.append(input[j])

    for i in values:
        if values.count(i) > 1:
            raise KeyError("Invalid list. Try again!")
    
    inverted = {}
    for i in values:
        inverted[i] = keys[values.index(i)]

    return inverted


def favorite_color(favorites: dict[str, str]) -> str:
    """This function analyzes a user-inputted dictionary that has the names of people and their favorite colors, and returns the most popular favorite color."""
    if len(favorites) == 0:
        return ''
        
    colors = []
    count = []
    final_colors = []
    for i in favorites:
        colors.append(favorites[i])

    for i in colors:
        count.append(colors.count(i))
        final_colors.append(i)
        for j in colors:
            if i == j:
                colors.pop(colors.index(j))
    
    max_value = max(count)
    indices = []
    
    for i in range(len(count)):
        if count[i] == max_value:
            indices.append(i)

    return final_colors[indices[0]]


def count(input: list[str]) -> dict[str, int]:
    """This function takes a user-inputted list and returns a dictionary with each unique element as the keys and their corresponding counts as the values.python -m tools.submission exercises/ex06"""
    final_dict = {}
    if len(input) == 0:
        return final_dict
    j = 0
    for i in input:
        final_dict[i] = input.count(i)
        while j < len(input):
            if input[j] == i:
                input.pop(j)
            else:
                j += 1

    return final_dict