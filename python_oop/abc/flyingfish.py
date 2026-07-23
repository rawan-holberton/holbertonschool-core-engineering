#!/usr/bin/env python3
"""Module demonstrating multiple inheritance with FlyingFish."""


class Fish:
    """Class representing a fish."""

    def swim(self):
        """Print the swimming behavior of a fish."""
        print("The fish is swimming")

    def habitat(self):
        """Print the habitat of a fish."""
        print("The fish lives in water")


class Bird:
    """Class representing a bird."""

    def fly(self):
        """Print the flying behavior of a bird."""
        print("The bird is flying")

    def habitat(self):
        """Print the habitat of a bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class representing a flying fish using multiple inheritance."""

    def fly(self):
        """Print the flying fish behavior."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print the flying fish swimming behavior."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print the flying fish habitat."""
        print("The flying fish lives both in water and the sky!")
