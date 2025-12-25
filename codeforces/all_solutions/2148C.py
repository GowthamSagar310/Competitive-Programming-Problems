def get_points(gap, pos_diff):
    if gap&1:
        if pos_diff:
            return gap
        else:
            return gap-1
    else:
        if pos_diff:
            return gap-1
        else:
            return gap

for _ in range(int(input())):
    n, tt = map(int, input().split())
    reqs = []
    ct, cp = 0, 0
    points = 0

    for _ in range(n):

        t, pos = map(int, input().split())
        points += get_points(t-ct, pos!=cp)
        ct, cp = t, pos
    
    points += tt-ct
    print(points)    
    
    # gap even, change pos -> gap-1 points
    # gap even, no change pos -> gap points
    # gap odd, change pos -> gap points
    # gap odd, no change pos -> gap-1 points
    
    """
    0 0
    1 1 
    2 1 gap = 2, pos_diff = True -> points += gap-1
    3 0
    4 0 gap = 2, pos_diff = True -> points += gap-1

    ==================

    0 0
    1 1 gap = 1, pos_diff = True -> points += gap 1
    2 0
    3 1
    4 0 gap = 3, pos_diff = True -> points += gap 3
    5 
    6
    7   points += gap -> 3

    ==================

    0 0
    1 0 gap = 1, pos_diff = False -> points += gap-1 0
    2 0 gap = 1, pos_diff = False -> points += gap-1 0
    3 1
    4 0
    5 1
    6 1 gap = 4, pos_diff = True -> points += gap-1 3
    7 0
    8 1
    9 0 gap = 3, pos_diff = True -> points += gap 3
    """