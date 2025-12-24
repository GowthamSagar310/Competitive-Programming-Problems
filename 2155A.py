for _ in range(int(input())):
    n = int(input())

    # simulation
    # a, b = n, 0 
    # total = 0
    # while a > 1 or b > 1:
    #     total += (a // 2) + (b // 2)
    #     b = (a // 2) + (b // 2 + b % 2)
    #     a = (a % 2) + (a // 2)
    # print(total+1)


    # winner's group
    # there are n players at the start
    # given the nature of the game, there will be only one team at the end in this group
    # and there are no additions in this group
    # so, n-1 matches should be been played at some point. 


    # loser's group
    # from the above n-1 matches, loser's group would have got n-1 teams 
    # out of these, only 1 remains at the end based on same logic above
    # so, n-2 matches should have been played till the end. 
    
    # at last, 1 team from both the groups are remained, which consitutes to one match
    
    # because the problem is unidirectional, there if flow in only one direction
    # that is why we can simply calculate the total matches. 

    print(n-1 + n-2 + 1)