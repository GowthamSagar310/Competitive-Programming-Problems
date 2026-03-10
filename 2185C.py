for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    maxi = 1
    start = end = arr[0]
    for i in range(1, n):
        if arr[i]-arr[i-1] <= 1:
            start = min(start, arr[i-1])
            end = max(end, arr[i])
        else:
            start = end = arr[i]
        maxi = max(maxi, end-start+1)
    print(maxi)
