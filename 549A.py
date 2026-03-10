n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(input())

def is_valid(i, j):
    return i > 0 and j > 0

count = 0
for i in range(1, n):
    for j in range(1, m):
        curr = matrix[i][j]
        if curr != "x":
            left = matrix[i][j-1]
            top = matrix[i-1][j]
            ud = matrix[i-1][j-1]
            if "".join(sorted(curr + left + top + ud)) == "acef":
                count += 1
print(count)