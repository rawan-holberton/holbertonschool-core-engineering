#!/usr/bin/env python3
"""Module containing an abstract Animal class and its subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class representing an animal."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        pass


class Dog(Animal):
    """Class representing a dog."""

    def sound(self):
        """Return the sound made by a dog."""
        return "Bark"


class Cat(Animal):
    """Class representing a cat."""

    def sound(self):
        """Return the sound made by a cat."""
        return "Meow"
