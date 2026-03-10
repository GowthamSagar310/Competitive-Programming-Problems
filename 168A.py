n, x, y = map(int, input().split())

"""

(100 * x) / n => percentage of x
we need atleast y percentage 

(100 * (x+k)) / n >= y

100 * (x + k) = y * n
x + k = ceil((y * n) / 100)
"""

ceil_val = (y * n + 100 - 1) // 100
print(max(0, ceil_val - x))