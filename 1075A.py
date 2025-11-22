n = int(input())
x, y = map(int, input().split())

# the shortest between (x1, y1) to (x2, y2) in coordinate system ?
# Chebyshev distance
# lets say it take "t" steps to move from point 1 to point 2
# t should be >= abs(x2-x1)
# t should be >= abs(y2-y1)
# because on both directions, the distance must be covered
# observation 1: t >= max(dx, dy)

# we know that we can always reach from point 1 to point 2 in t steps (somehow)
# we can greedily try to take diagonal steps (reduces both x,y by 1 at same time)
# and cover the remaining in straight direction (either x or y)
# minimum steps in diagonal direction = min(dx, dy)
# after that they are going to meet a point (x3, y3) which either aligns with one of the axis

# t = min(dx, dy) + (y2-y3) if x2 = x3
# t = min(dx, dy) + (y2-y1) - min(dx, dy)
# t = (y2 - y1) if x2 = x3 (x is aligned before y because dx <= dy)
# t = max(dx, dy)

# t = min(dx, dy) + (x2-x3) if y2 = y3
# t = min(dx, dy) + (x2-x1) - min(dx, dy)
# t = (x2 - x1) if y2 = y3 (y is aligned before x because dy <= dx)
# t = max(dx, dy)
 

k1x, k1y = 1, 1
k2x, k2y = n, n

k1_distance = max(x-1, y-1)
k2_distance = max(n-x, n-y)

# print(k1_distance, k2_distance)
print("White" if k1_distance <= k2_distance else "Black")