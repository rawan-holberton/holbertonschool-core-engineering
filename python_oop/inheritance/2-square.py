#!/usr/bin/env python3
"""Square class module."""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initialize a square.

        Args:
            size (int): Size of the square.
        """
        self.integer_validator("size", size)

        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return the square description.

        Returns:
            str: Square representation.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
