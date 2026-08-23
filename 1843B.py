for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    s = 0
    cs = 0
    ops = 0
    i = 0
    while i < n:
        if arr[i] < 0:
            while i < n and arr[i] <= 0:
                s += abs(arr[i])
                i += 1
            ops += 1
        else:
            s += arr[i]
            i += 1
    print(s, ops)
