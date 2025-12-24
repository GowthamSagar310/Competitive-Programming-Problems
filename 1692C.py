def is_valid_point(x, y):
    if x >= 0 and x < 8 and y >= 0 and y < 8:
        if matrix[x][y] == "#":
            return True
    return False

def solve(matrix):
    for r in range(8):
        for c in range(8):
            if matrix[r][c] == "#":
                if (
                    is_valid_point(r-1, c-1) and
                    is_valid_point(r-1, c+1) and 
                    is_valid_point(r+1, c-1) and 
                    is_valid_point(r+1, c+1)
                ):
                    return [r+1, c+1]


for _ in range(int(input())):
    matrix = []
    input()
    for _ in range(8):
        matrix.append(input())
    print(*solve(matrix))