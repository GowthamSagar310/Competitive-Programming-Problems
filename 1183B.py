for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    """
    - can change the values by [-k, +k]
    - all the values should be same after changing
    - it should be maximized
    
    
    1 1 1 2 3
    k = 1
    range for 3 = [2, 4]
    range for 2 = [1, 3] = combining with above range is [2, 3]
    range for 1 = [0, 2] = combining with above range is [2]
    
    """
    arr.sort()
    l = float("-inf")
    r = float("inf")
    for i in range(n-1, -1, -1):
        new_l = arr[i]-k
        new_r = arr[i]+k
        if new_r < l:
            r = -1
            break
        else:
            l = max(l, new_l)
            r = min(r, new_r)
    print(r)