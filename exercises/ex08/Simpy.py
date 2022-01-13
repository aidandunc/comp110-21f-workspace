"""Utility class for numerical operations."""

from __future__ import annotations
from typing import Union

__author__ = "730530326"


class Simpy:
    """A class meant to represent functions of Numpy."""
    values: list[float]

    def __init__(self, final: list[float]):
        """Initialization constructor."""
        self.values: list[float] = final

    def __str__(self) -> str:
        """Simpy conversion."""
        return f'Simpy({self.values})'

    def fill(self, value: float, number: int) -> None:
        """Fills in the values list with a given floating point value a certain number of times."""
        self.values = []
        for i in range(number):
            self.values.append(value)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Creates a Simpy with a values list a range from a specified starting and stopping point with a specified interval."""
        intermediary = []
        for i in range(int(stop // step)):
            if start + (i * step) == stop:
                None
            else:    
                intermediary.append(start + (i * step))
                
        self.values = intermediary

    def sum(self) -> float:
        """Sums the value list."""
        return sum(self.values)

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Adds the values of a Simpy values list to either the values of another Simpy or a float value."""
        total_list = []

        if isinstance(rhs, Simpy):
            for i in range(len(self.values)):
                total_list.append(self.values[i] + rhs.values[i])
        else:
            for i in range(len(self.values)):
                total_list.append(self.values[i] + rhs)

        return Simpy(total_list)

    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Sets the values of a Simpy values list to the powers of another float or the values of a Simpy values list."""
        total_list = []

        if isinstance(rhs, Simpy):
            for i in range(len(self.values)):
                total_list.append(self.values[i] ** rhs.values[i])
        elif isinstance(rhs, float):
            for i in range(len(self.values)):
                total_list.append(self.values[i] ** rhs)

        return Simpy(total_list)

    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Tests to see if either two Simpy values list or the values of Simpy list with a float value."""
        total_list = []

        if isinstance(rhs, Simpy):
            for i in range(len(self.values)):
                total_list.append(self.values[i] == rhs.values[i])
        elif isinstance(rhs, float):
            for i in range(len(self.values)):
                total_list.append(self.values[i] == rhs)

        return total_list

    def __gt__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Tests to see if the values of a Simpy values list are greater than a specified value or the values of another Simpy values list."""
        total_list = []

        if isinstance(rhs, Simpy):
            for i in range(len(self.values)):
                total_list.append(self.values[i] > rhs.values[i])
        elif isinstance(rhs, float):
            for i in range(len(self.values)):
                total_list.append(self.values[i] > rhs)

        return total_list

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Combines above methods to mask Simpy values with an int or bool and returns either a float or a Simpy."""
        returning_list = []
        if isinstance(rhs, int):
            return(self.values[rhs])
        if isinstance(rhs, list):
            for i in range(len(rhs)):
                if rhs[i] is True:
                    returning_list.append(self.values[i])
            return Simpy(returning_list)