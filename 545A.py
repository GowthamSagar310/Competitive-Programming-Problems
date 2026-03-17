n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

res = [0 for _ in range(n)]

for i in range(n):
    for j in range(n):
        val = matrix[i][j]
        if i != j:
            if val == 1: res[i] = -1
            elif val == 2: res[j] = -1
            elif val == 3: res[i] = -1; res[j] = -1

total = res.count(0)
print(total)
for i in range(n):
    if res[i] == 0:
        print(i+1, end = " ")