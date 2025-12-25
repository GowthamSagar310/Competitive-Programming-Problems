n = int(input())

r = c = (2*n)+1
matrix = [
    ["" for _ in range(c)] for _ in range(r)
]

# middle column
mc = c // 2
num = 0
for i in range(c):
    matrix[i][mc] = num
    num += 1 if i < mc else -1

# left half
for i in range(mc-1, -1, -1):
    for j in range(r):
        if matrix[j][i+1] == " " or matrix[j][i+1] == 0:
            matrix[j][i] = " "
        else:
            matrix[j][i] = matrix[j][i+1]-1

# right half 
for i in range(mc+1, c):
    for j in range(r):
        if matrix[j][i-1] == "" or matrix[j][i-1] == 0:
            continue
        else:
            matrix[j][i] = matrix[j][i-1]-1

for row in matrix:
    print(" ".join(map(str, row)))
