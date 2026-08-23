n, m = map(int, input().split())
grid = []
ones = []
for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)
    for j in range(m):
        if grid[i][j] == 1:
            ones.append((i, j))

corners = [(0, 0), (0, m-1), (n-1, 0), (n-1, m-1)]
distances = []
for ci in corners:
    for oi in ones:
        x, y = ci
        xo, yo = oi
        distances.append((ci, oi, (x-xo) ** 2 + (y-yo) ** 2))
distances.sort(key=lambda x: x[2], reverse=True)

def fill_gap(x, y, xo, yo):
    for i in range(x, xo+1):
        for j in range(y, yo+1):
            grid[i][j] = 1
    filled = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                filled += 1 
    return filled

ops = 0
total_filled = 0
for ci, oi, d in distances:
    x, y = ci
    xo, yo = oi
    if grid[x][y] != 1:
        total_filled = fill_gap(min(x, xo), min(y, yo), max(x, xo), max(y, yo))
        ops += 1
        if total_filled == m * n: break
print(ops)
