n = int(input())

"""

1378 ^ n

8 n = 1
4 n = 2
2 n = 3
6 n = 4 % 4 = 0
8 n = 5 % 4 = 1
"""
if n == 0:
    print(1)
else:
    r = n % 4
    if r == 1:
        print(8)
    elif r == 2:
        print(4)
    elif r == 3:
        print(2)
    else:
        print(6)