#!/usr/bin/env python3
"""Module containing a VerboseList class extending Python's list."""


class VerboseList(list):
    """A list subclass that prints notifications on modifications."""

    def append(self, item):
        """Add an item and print a notification message."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list and print the number of added items."""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Remove an item and print a notification message."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return an item with a notification message."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
