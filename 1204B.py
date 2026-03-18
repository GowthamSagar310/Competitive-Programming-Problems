n, l, r = map(int, input().split())

"""
each element is even except for 1, and there must be half.
if 2 has to be there, 1 should be part of the array
if 4 has to be there, 2, 1 should be part of the array

if n == 1: max and min should be 1, because half of cannot be present for others

maximum number of unique numbers = r
one of them is 1. 
so r-1 more unique numbers (2, 4, 8 etc.)


maximum sum -> from bigger unqiue values
mimum sum -> smaller values

"""

minimal = 1 * (n-l) + (2 ** (l) - 1)
maximal = (2 ** (r) - 1) + (n-r) * (2 ** (r-1))

print(minimal, maximal)