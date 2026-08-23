for _ in range(int(input())):
    n, x, y = map(int, input().split())
    """
    there are players
    n-1 games

    p1 p2 p3 p4 p5
       p1 p1 p4 p4

    8 1 2 

    7 - 2 = 5 odd [p1, p2] [p1, p3]
    5 - 1 = 4 even [p4, p1]
    4 - 2 = 2 even [p4, p5] [p4, p6]
    2 - 1 = 1 [p6, p7]
    1 - 1 = 0 [p7, p8]

    4 0 1
    p1 p2 = p1
    p1 p3 = p3
    p3 p4 = p4
    """

    if (x == 0 and y == 0) or (x != 0 and y != 0):
        print(-1)
    elif (n-1) % max(x, y) != 0:
        print(-1)
    else:
        k = max(x, y)
        ans = []
        l, r = 1, 2
        while r <= n:
            if k:
                ans.append(l)
                r += 1
                k -= 1
            else:
                l = r
                r = l+1
                ans.append(l)
                k = max(x, y)-1
        print(*ans)
