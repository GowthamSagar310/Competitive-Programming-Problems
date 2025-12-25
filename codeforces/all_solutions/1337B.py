for _ in range(int(input())):
    h, n, m = map(int, input().split())

    # spell 1 -> (h // 2) + 10 
    # if h is less 20, spell 1 is going to increase the h of dragon
    # so, bring the h to < 20, using spell 1

    # spell 2 -> h-10
    # use after h of dragon is < 20

    while n and h > 20:
        h = (h // 2) + 10
        n -= 1
    if h <= 0:
        print("YES")
    else:
        can_decrease = m * 10
        if h <= m * 10:
            print("YES")
        else:
            print("NO")