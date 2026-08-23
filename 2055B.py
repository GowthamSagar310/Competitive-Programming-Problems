for _ in range(int(input())):
    n = int(input())
    current = list(map(int, input().split()))
    required = list(map(int, input().split()))

    """
    - there can be only one index where c < r
    - if there are multiple is not possible to arrange. 
    """

    d = -1
    for i in range(n):
        c, r = current[i], required[i]
        if c < r:
            if d != -1:
                d = -2
                break
            d = r-c
    
    if d == -2: print("NO"); continue
    if d == -1: print("YES"); continue

    possible = True
    for i in range(n):
        c, r = current[i], required[i]
        if c >= r:
            if c-d < r:
                possible = False
                break
    print("YES" if possible else "NO") 