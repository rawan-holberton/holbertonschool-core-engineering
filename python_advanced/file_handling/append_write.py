#!/usr/bin/env python3
"""Module for appending text to a UTF-8 file."""


def append_write(filename="", text=""):
    """Append a string to a text file and return character count."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
