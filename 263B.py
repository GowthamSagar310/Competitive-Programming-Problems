n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

if k > n:
    print(-1)
else:
    print(arr[n-k], arr[n-k])