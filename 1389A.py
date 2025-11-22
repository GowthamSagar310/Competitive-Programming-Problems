for _ in range(int(input())):
    
    l, r = map(int, input().split())

    # find two integers x ,y such that
    
    # l <= x < y <= r
    # l <= lcm(x, y) <= r
    # l.g <= x * y <= r.g

    # x * y >= l.g
    # x >= l
    # x.g >= l.g


    # lcm(l, 2*l) = (l * 2l)/l = 2*l
    # if 2l <= r, then it can be the answer
    # l <= l < 2l <= r
    
    if 2*l <= r:
        print(l, 2*l)
    else:
        print(-1, -1)
