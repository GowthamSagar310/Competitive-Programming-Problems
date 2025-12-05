for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr1 = sorted(arr)
    m1, m2 = arr1[-1], arr1[-2]
    res = []
    for val in arr:
        if val != m1:
            res.append(val-m1)
        else:
            res.append(val-m2)
    print(*res)