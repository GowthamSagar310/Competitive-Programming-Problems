n = int(input())
arr = list(map(int, input().split()))
arr_i = sorted([(val, i) for i, val in enumerate(arr)], reverse=True)
ans = [0] * n
ans[arr_i[0][1]] = 1
for i in range(1, n):
    val, index = arr_i[i]
    # if equal to previous value -> same rank
    if val == arr_i[i-1][0]:
        ans[arr_i[i][1]] = ans[arr_i[i-1][1]]
    else:
        ans[arr_i[i][1]] = i+1
print(*ans)