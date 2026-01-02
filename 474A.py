dir = input()
s = input()

grid = [
    list("qwertyuiop"),
    list("asdfghjkl;"),
    list("zxcvbnm,./")
]

m = {}
for i in range(3):
    for j in range(10):
        m[grid[i][j]] = (i, j)

res = []
for l in s:
    i, j = m[l]
    if dir == "R":
        res.append(grid[i][j-1])
    else:
        res.append(grid[i][j+1])

print("".join(res))