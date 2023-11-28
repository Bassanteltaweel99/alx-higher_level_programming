#!/usr/bin/python3

"""Print the alphabet in lowercase, not followed by a new line."""
for b in range(ord ('a'), ord ('z') + 1):
    print("{:c}".format (b), end="")
