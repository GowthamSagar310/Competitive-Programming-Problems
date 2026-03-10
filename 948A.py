r, c = map(int, input().split())

matrix = []
for _ in range(r):
    matrix.append(list(input()))

def is_valid(i, j, r, c):
    if 0 <= i < r and 0 <= j < c:
        return True
    return False

def solve(matrix, r, c):
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == "W":
                # close all 4 directions if possible
                for dr, dc in zip([+1, 0, 0, -1], [0, +1, -1, 0]):
                    row, col = i+dr, j+dc
                    if is_valid(row, col, r, c):
                        if matrix[row][col] == "S":
                            return False
                        elif matrix[row][col] == ".":
                            matrix[row][col] = "D"
    return True

if solve(matrix, r, c):
    print("Yes")
    for row in matrix:
        print("".join(row))
else:
    print("No")