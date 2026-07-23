#!/usr/bin/env python3
"""BaseGeometry class module."""


class BaseGeometry:
    """Represents a base geometry class."""

    def area(self):
        """Calculate the area of the shape.

        Raises:
            Exception: Always, because the area is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name (str): Name of the value being validated.
            value (int): Value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
