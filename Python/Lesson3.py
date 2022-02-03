# Write a program to:
# Find all numbers, between 2000 and 3200 (both included),
# that are divisible by 7, but are not a multiple of 5
# The numbers obtained should be returned on a single line. seperated by commas.

for x in range(2000, 3200):
    if x % 7 == 0 and not x % 5 == 0:
        print(x, end=',')
    else:
        continue
