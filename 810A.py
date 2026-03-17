from math import ceil
n, k = map(int, input().split())
arr = list(map(int, input().split()))

"""
total + (k * x) = (n + x) * (k-0.5)


total = nk - 0.5n- x0.5
0.5x = nk - 0.5n - total
x = 2nk - n - 2*total
"""

x = max(0, 2 * n * k - n - 2 * sum(arr))
print(x)


