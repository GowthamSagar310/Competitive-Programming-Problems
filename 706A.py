from math import sqrt
a, b = map(int, input().split())
n = int(input())
min_time = float("inf")
for _ in range(n):
    x, y, v = map(int, input().split())
    distance = sqrt((a-x) ** 2 + (b-y) ** 2)
    if distance == 0:
        min_time = 0
    else:
        min_time = min(min_time, distance / v)
print(min_time)