n, m = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, list(input()))))

count = 0

column_max = [0] * m
for j in range(m):
    maxi = max(matrix[i][j] for i in range(n))
    column_max[j] = maxi

for i in range(n):
    for j in range(m):
        if matrix[i][j] == column_max[j]:
            count += 1
            break
print(count)