# Create 2 new Python files. In one file
# Write a function that will generate a number between 1 and 6.
# Make this a module called dice.

from random import randint


def diceroll():
    return randint(1, 6)
