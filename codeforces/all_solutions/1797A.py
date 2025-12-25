def adjacent_points(n, m, x, y):
    count = 0
    if x-1 >= 1: count += 1
    if x+1 < n+1: count += 1
    if y-1 >= 1: count += 1
    if y+1 < m+1: count += 1
    return count

# other way to count adjacent sides 
# if on the corner (4 corners of the rectangle) -> 2
# if on the border (touching one of the side) -> 3
# if in the middle (every other cell) -> 4

# def adjacent_sides_v2(n, m, x, y):
#     if (x == 1 or x == n) and (y == 1 or y == n): return 2
#     if (x == 1 or x == n or y == 1 or y == n): return 3
#     return 4


for _ in range(int(input())):
    
    n, m = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())

    # block one of the points completely
    # how many adjacent blocks to a given point ? 
    print(min(adjacent_points(n, m, x1, y1), adjacent_points(n, m, x2, y2)))
    