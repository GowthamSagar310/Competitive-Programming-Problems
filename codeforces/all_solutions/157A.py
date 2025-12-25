n = int(input())
row_sum = [0] * n
col_sum = [0] * n
for i in range(n):
    row = list(map(int, input().split()))
    for index, val in enumerate(row):
        row_sum[i] += val
        col_sum[index] += val

winning = 0
for i in range(n):
    for j in range(n):
        if col_sum[j] > row_sum[i]:
            winning += 1
print(winning)