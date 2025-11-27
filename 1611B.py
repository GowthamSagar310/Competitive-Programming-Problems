for _ in range(int(input())):
    a, b = map(int, input().split())
    
    # there cannot be more teams than min(a, b)
    # there cannot be more teams than (a + b) // 4

    # say we can build k teams
    # ---- + ---- + ---- + .... k teams
    
    # requirement 1 -> each team must have 1P, 1M
    # PM-- + PM-- + PM-- + .... k teams
    # Note if there are only K-1 P, then we are limited to K-1 teams

    # requirement 2 -> each team must have 4 people
    # we already used 2K people in req 1
    # we need 2K more in req 2
    # to form k teams, we need a + b - 2k more (after using 2k)
    # a + b - 2k >= 2k 
    # a + b >= 4k 
    # k <= (a + b) // 4
    
    # this to form k teams, 
    # we need min((a+b)//4, min(a,b))
    # after this, some thing will run out. 
    

    # how do we know min(min(a, b), total // 4) teams will be achievable ? 
    # how are we sure that this number is always achievable ? 

    # say, we are forming k teams
    # add 1p, 1m in each team (and say we have more)
    # and we have a + b - 2k >= 2k
    # meaning we can comfortably place remaining to form teams
    # and left overs are useless anyway
    # so we can reach the number always, or else we will have less teams

    # O(1)
    # print(min(min(a, b), (a + b) // 4))

    # binary search solution

    def is_possible_to_form(k):
        # k teams -> 4k people
        # condition 1 4k <= a + b (already covered in the upper limit of search space)
        # condition 2 in each team atleast 1 a and 1 b should be present 
        # so k <= a and k <= b

        return k <= a and k <= b
        
    l, r = 0, (a + b) // 4
    while l <= r:
        mid = (l + r) >> 1
        if is_possible_to_form(mid):
            l = mid+1
        else:
            r = mid-1
    print(r)