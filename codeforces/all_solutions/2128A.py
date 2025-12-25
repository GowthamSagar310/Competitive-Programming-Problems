for _ in range(int(input())):
    n, c = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    i = n-1
    multiplier = 0
    removed = 0
    while i >= 0:
        arr[i] *= (2 ** multiplier)
        if arr[i] <= c:
            removed += 1
            multiplier += 1
        i -= 1
    print(n-removed)
        
