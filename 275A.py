grid = [list(map(int, input().split())) for _ in range(3)]

ans = [[0 for _ in range(3)] for _ in range(3)]

def mark_grid(i, j):
    ans[i][j] += 1
    if i-1 >= 0: ans[i-1][j] += 1
    if i+1 < 3: ans[i+1][j] += 1
    if j-1 >= 0: ans[i][j-1] += 1
    if j+1 < 3: ans[i][j+1] += 1

for i in range(3):
    for j in range(3):
        if grid[i][j] & 1:
            mark_grid(i, j)

for i in range(3):
    for j in range(3):
        if ans[i][j] & 1:
            ans[i][j] = 0
        else:
            ans[i][j] = 1

for row in ans:
    print("".join(map(str, row)))



