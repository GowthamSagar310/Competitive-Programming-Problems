from math import gcd
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    # the idea here is that
    # if the number is not in its right position (since it is a permutation, this can be known.)
    # this difference is what we need as k to make the array sorted.
    # but there will be different difference values for each number
    # to accomodate the movements, we need a value which produce all the differences
    # meaning, some value which divides all these differences
    # so which this value, if swaps are made, numbers can be moved to their right destinations

    # that number which divides everything is gcd
    min_diff = 0
    for i, val in enumerate(arr):
        if val != i+1:
            min_diff = gcd(min_diff, abs(val-(i+1)))
    print(min_diff)
