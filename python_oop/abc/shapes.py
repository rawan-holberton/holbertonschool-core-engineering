#!/usr/bin/env python3
"""Module containing abstract Shape class and shape implementations."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class representing a geometric shape."""

    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Class representing a circle."""

    def __init__(self, radius):
        """Initialize a circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate and return the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize a rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of any shape object.

    Uses duck typing by calling area() and perimeter()
    without checking the object's type.
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
