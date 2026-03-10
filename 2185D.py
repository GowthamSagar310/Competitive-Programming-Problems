for _ in range(int(input())):
    n, m, h = map(int, input().split())
    arr = list(map(int, input().split()))
    temp = arr[:]

    last_processed_crash = [-1] * n
    last_max_crash = -1
    level = 1

    for _ in range(m):
        b, c = map(int, input().split())

        if last_processed_crash[b-1] < last_max_crash:
            arr[b-1] = temp[b-1]
            last_processed_crash[b-1] = last_max_crash
        
        arr[b-1] += c
        
        if arr[b-1] > h:
            arr[b-1] = temp[b-1]
            last_max_crash = level
        
        level += 1

    for i in range(n):
        if last_processed_crash[i] < last_max_crash:
            arr[i] = temp[i]
    
    print(*arr)