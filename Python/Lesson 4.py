# Given an integer n, write a python function
# which returns a times table grid for all the integers between 1 and n.
# The grid should be separated by tabs and new lines.

n = int(input('Enter whole number: '))
for row in range(1, n + 1):
    for col in range(1, n + 1):
        print(row*col, end="\t")
    print()
