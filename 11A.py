count = 0
n, d = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(1, n):
    if arr[i] <= arr[i-1]:
        diff = arr[i-1]-arr[i]
        increase = (diff // d) + 1
        arr[i] = arr[i] + increase * d
        count += increase
print(count)