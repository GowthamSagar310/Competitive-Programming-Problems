for _ in range(int(input())):
    p1, p2, p3 = map(int, input().split())

    # because the p1 + p2 + p3 after each round increases by 2
    # if the sum is odd at some point, we know that it would not have been possible 

    if (p1 + p2 + p3) & 1:
        print(-1)
    else:
        
        # minimum p1 draws are always possible
        # but how do we take out p1 points from p2 and p3 ? 
        # we do it in such a way that both are closer

        # p1 draws + 
        # remaining points = p2+p3-p1 
        # from these, if p2 = p3, max possible draws are (p2 + p3 - p1) / 2

        # of if they are not closer, meaning they are not equal
        # p2 draws are always possible, so we just have to see which is minimum

        # why minimum ? because if p2 == p3 (after removing p1), p2 == (p2 + p3 - p1) / 2
        # and if p2 + p3 are not equal, because p1 <= p2 <= p3, p2 is always smaller
        
        print(p1 + min(p2, (p2 + p3 - p1) // 2))
