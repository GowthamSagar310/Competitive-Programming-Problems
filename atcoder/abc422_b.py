h, w = map(int, input().split())
rows = []
for _ in range(h):
    rows.append(input())
flag = False
for i in range(h):
    for j in range(w):
        if rows[i][j] == "#": # black

            blacks = 0
            # up
            if i-1 >= 0 and rows[i-1][j] == "#": blacks += 1
            # down
            if i+1 < h and rows[i+1][j] == "#": blacks += 1
            # left 
            if j-1 >= 0 and rows[i][j-1] == "#": blacks += 1
            # right
            if j+1 < w and rows[i][j+1] == "#": blacks += 1

            if blacks != 2 and blacks != 4:
                flag = True
                break
    if flag:
        break
print("No" if flag else "Yes")
