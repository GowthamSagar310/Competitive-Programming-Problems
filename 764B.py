n = int(input())
arr = list(map(int, input().split()))
for i in range(n//2):
    if i % 2 == 0:
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
print(*arr)