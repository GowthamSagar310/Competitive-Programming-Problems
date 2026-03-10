from math import sqrt
n, k = map(int, input().split())
points = []
for _ in range(n):
    points.append(tuple(map(int, input().split())))

distance = 0
for i in range(1, n):
    x1, y1 = points[i-1]
    x2, y2 = points[i]
    distance += sqrt((x2-x1) ** 2 + (y2-y1) ** 2)

print(k * (distance / 50))

"""
speed = distance / time
time = distance / speedd
""" 