for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    # if either side of the element is made empty, then 1 else 0

    # 1 3 5 4 7 2 
    # 7 7 7 7 7 2
    # 1 1 1 1 1 1
    # 1 0 0 0 1 1

    minis, maxis = [], [0] * n
    mini, maxi = float("inf"), float("-inf")
    for i in range(n): mini = min(mini, arr[i]); minis.append(mini)
    for i in range(n-1, -1, -1): maxi = max(maxi, arr[i]); maxis[i] = maxi 
    res = []
    for i in range(n):
        mini, maxi = minis[i], maxis[i]
        if arr[i] == mini or arr[i] == maxi:
            res.append("1")
        else:
            res.append("0")
            
    print("".join(res))
