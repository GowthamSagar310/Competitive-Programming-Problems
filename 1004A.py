n, d = map(int, input().split())
arr = list(map(int, input().split()))

count = 2
for i in range(1, n):

    diff = arr[i]-arr[i-1]
    if diff > 2 * d:
        count += 2
    elif diff == 2 * d:
        count += 1

print(count)