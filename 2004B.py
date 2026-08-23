for _ in range(int(input())):
    l, r = map(int, input().split())
    L, R = map(int, input().split())
    
    """
    - 3 4 5 6 7
    -       6 7

    - 2 3 4 5
    - 2 3 4 5

    - 1 2 3
    -     3 4 5
    -     
    """

    if r < L or R < l:
        # these are not overlapping. 
        # so, closing one door inbetween is enough. 
        print(1)
    else:
        l_overlap = max(l, L)
        r_overlap = min(r, R)
        if l != L: l_overlap -= 1
        if r != R: r_overlap += 1
        print(r_overlap - l_overlap)