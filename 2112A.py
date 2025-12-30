for _ in range(int(input())):
    a, x, y = map(int, input().split())
    
    # pair wise distinct 
    # b has to be closer to x and y than a

    if (a < x and a < y) or (a > x and a > y):
        # pick x
        print("YES")
    else:
        # a is in between of x and y
        # there is no way b can be choosen that 
        # is closer to both x and y than a
        
        # cannot choose a
        print("NO")
        
    