for _ in range(int(input())):
    n, k, q = map(int, input().split())
    arr = list(map(int, input().split()))
    batches = []

    count = 0
    for i in range(n):
        if arr[i] <= q:
            count += 1
        else:
            if count >= k:
                batches.append(count)
            count = 0
        
    if count >= k: batches.append(count)
    total = 0
    for b in batches:
        t = b-k+1
        total += (t * (t + 1)) // 2
    
    print(total)