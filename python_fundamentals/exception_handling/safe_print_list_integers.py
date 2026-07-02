#!/usr/bin/env python3
"""Module that safely prints integers from a list."""


def safe_print_list_integers(my_list=[], x=0):
    """Print the first x integers of a list safely."""
    count = 0

    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
        except IndexError:
            break

    print()
    return count
