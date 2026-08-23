def is_possible_row(i,j):
    while i >= 0:
        if grid[i][j] != "1":
            return False
        i -= 1
    return True

def is_possible_col(i,j):
    while j >= 0:
        if grid[i][j] != "1":
            return False
        j -= 1
    return True

for _ in range(int(input())):
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(input())
    possible = True    
    for i in range(1, n):
        for j in range(1, m):
            if grid[i][j] == "1":
                if not is_possible_row(i, j) and not is_possible_col(i, j):
                    possible = False
                    break
        if not possible:
            break
    print("YES" if possible else "NO")