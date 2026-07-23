#!/usr/bin/env python3
"""Rectangle class module."""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle."""

    def __init__(self, width, height):
        """Initialize a rectangle.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The rectangle area.
        """
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description.

        Returns:
            str: Rectangle representation.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
