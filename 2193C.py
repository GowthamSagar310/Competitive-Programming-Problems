for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    queries = []
    for _ in range(q):
        l, r = map(int, input().split())
        queries.append((l-1, r-1))

    for i in range(n):
        if a[i] < b[i]:
            a[i] = b[i]
        
    for i in range(n-2, -1, -1):
        if a[i+1] > a[i]:
            a[i] = a[i+1]
    
    pre = [a[0]]
    for i in range(1, n):
        pre.append(pre[-1] + a[i])

    ans = [ ]
    for l, r in queries:
        ans.append(pre[r] - (pre[l-1] if l > 0 else 0))
    print(*ans)

