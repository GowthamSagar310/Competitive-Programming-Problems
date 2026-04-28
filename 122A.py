n = int(input())

"""
should be divisible by number which contains only 4s
should be divisible by number which contains only 7s
should be divisible by number which contains only 4s and 7s

4 44 444
7 77 777

47 477
447 474

74 744
774 747

"""

print("YES" if any(n % val == 0 for val in [
    4, 44, 444,
    7, 77, 777,
    47, 477,
    447, 474,
    74, 744,
    747, 774
]) else "NO")