#!/usr/bin/env python3
"""Module for writing text to a UTF-8 file."""


def write_file(filename="", text=""):
    """Write a string to a text file and return character count."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
