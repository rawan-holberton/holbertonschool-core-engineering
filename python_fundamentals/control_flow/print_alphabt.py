#!/usr/bin/env python3

alphabet = ""

for letter in range(ord('a'), ord('z') + 1):
    if letter != ord('e') and letter != ord('q'):
        alphabet += chr(letter)

print("{}".format(alphabet))
