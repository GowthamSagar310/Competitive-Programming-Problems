def is_inside_board(x, y, n, m):
    if 1 <= x < n+1 and 1 <= y < m+1:
        return True
    return False

def is_isolated(x, y):
    for dx, dy in diff:
        r = x + dx
        c = y + dy
        if is_inside_board(r, c, n, m):
            return False
    return True

def solve():
    for row in range(1, n+1):
        for col in range(1, m+1):
            if is_isolated(row, col):
                return str(row) + " " + str(col)
    return "1 1"

for _ in range(int(input())): 
    n, m = map(int, input().split())

    # if knight is in x, y
    # (x-2, y+1) (x-2, y-1)
    # (x-1, y+1) (x-1, y-2)
    # (x+1, y+2) (x+1, y-2)
    # (x+2, y-1) (x+2, y+1)

    diff = [
        (-2, +1),
        (+2, +1),
        (-2, -1),
        (+2, -1),
        (+1, +2),
        (+1, -2),
        (-1, +2),
        (-1, -2)
    ]

    print(solve())        
