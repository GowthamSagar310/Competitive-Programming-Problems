from math import gcd
for _ in range(int(input())):
    a, b, k = map(int, input().split())

    g = gcd(a, b)
    if max(a // g, b // g) <= k:
        print(1)
    else:
        print(2)

    # cost is always either 1 or 2 
    # 2 is possible because using 0,1 or 1,0 to reach (0,0)
    # 1 is possible if
    # there exists a number "x" such that
    # 1. a = x . dx
    # 2. b = x . dy
    # 3. dx <= k and dy <= k
    # dx = (a / t)
    # dy = (b / t)
    # because we want dx <= k
    # it is better to choose the biggest number 
    # (not that there might be other nummbers that satisfy this.)
    # biggest number that we can choose that divides both a, b = gcd(a,b)