"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730484959"


class Simpy:
    """Simpy class."""
    values: list[float]

    def __init__(self, list: list[float]):
        """Initalizing."""
        self.values = list
    
    def __str__(self) -> str:
        """Outputting string."""
        return f"Simpy({self.values})"

    def fill(self, float_val: float, int_val: int) -> None:
        """Filling."""
        self.values = [float_val] * int_val

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Giving a range."""
        assert step != 0.0
        self.values = [start]
        while start != stop - step:
            start += step
            (self.values).append(start)
    
    def sum(self) -> float:
        """Summing the values."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adding two things."""
        if isinstance(rhs, float):
            newer_object: list[float] = []
            for i in self.values:
                newer_object.append(i + rhs)
            return Simpy(newer_object)
        else:
            new_object: list[float] = []
            assert len(rhs.values) == len(self.values)
            for i in range(0, len(self.values)):
                new_object.append(self.values[i] + rhs.values[i])
            return Simpy(new_object)
        
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Exponeting two things."""
        if isinstance(rhs, float):
            newer_object: list[float] = []
            for i in self.values:
                newer_object.append(i ** rhs)
            return Simpy(newer_object)
        else:
            new_object: list[float] = []
            assert len(rhs.values) == len(self.values)
            for i in range(0, len(self.values)):
                new_object.append(self.values[i] ** rhs.values[i])
            return Simpy(new_object)
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Equalizing."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for i in self.values:
                result.append(i == rhs)
            return result
        else:
            assert len(rhs.values) == len(self.values)
            for i in range(0, len(self.values)):
                result.append(self.values[i] == rhs.values[i])
            return result
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Greater than."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for i in self.values:
                result.append(i > rhs)
            return result
        else:
            assert len(rhs.values) == len(self.values)
            for i in range(0, len(self.values)):
                result.append(self.values[i] > rhs.values[i])
            return result
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Setting mask and comparing."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            result_list: list[float] = []
            i: int = 0
            while i < len(rhs):
                if rhs[i]:
                    result_list.append(self.values[i])
                i += 1
            return Simpy(result_list)

        