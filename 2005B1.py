from math import floor
for _ in range(int(input())):
    n, m, q = map(int, input().split())
    [L, R] = sorted(list(map(int, input().split())))
    d = list(map(int, input().split()))[0] #q == 1
    if d < L:
        print(L-1)
    elif d > R:
        print(n-R)
    else:
        # david is certainly caught if there is no where to go. 
        # the gap between L and R closes 2 per single move.
        print(floor((R-L) / 2))
