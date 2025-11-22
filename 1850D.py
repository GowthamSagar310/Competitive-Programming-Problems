for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    maxi = 1
    count = 1
    for r in range(1, n):
        if arr[r] - arr[r-1] <= k:
            count += 1
        else:
            count = 1
        maxi = max(maxi, count)
    print(n-maxi)
