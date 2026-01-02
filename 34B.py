n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
total = 0
for i in range(m):
    if arr[i] < 0:
        total += -arr[i]
    else:
        break
print(total)