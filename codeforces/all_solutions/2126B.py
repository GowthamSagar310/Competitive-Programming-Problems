for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    hikes = 0
    i = 0
    count = 0
    while i < n:
        if arr[i] == 0:
            count += 1
            if count == k:
                count = 0
                hikes += 1
                i += 1
        else:
            count = 0 
        i += 1
    print(hikes)