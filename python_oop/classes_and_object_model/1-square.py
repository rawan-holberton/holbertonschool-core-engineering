#!/usr/bin/env python3
"""Defines a Square class with a private size attribute."""


class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initialize a square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
