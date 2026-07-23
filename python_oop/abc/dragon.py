#!/usr/bin/env python3
"""Module demonstrating mixins with a Dragon class."""


class SwimMixin:
    """Mixin providing swimming ability."""

    def swim(self):
        """Print the swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Mixin providing flying ability."""

    def fly(self):
        """Print the flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class representing a dragon with multiple abilities."""

    def roar(self):
        """Print the dragon's roar."""
        print("The dragon roars!")
