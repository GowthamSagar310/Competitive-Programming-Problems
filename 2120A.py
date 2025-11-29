for _ in range(int(input())):
    l1, b1, l2, b2, l3, b3 = map(int, input().split())

    # l3 <= l2 <= l1
    # b3 <= b2 <= b1
    # rectangles are becoming smaller 

    # there are only 3 rectangles 
    # out of which l1, b1 is bigger

    # there are 4 combinations 
    #  ------- ----
    # |       |    |
    # |       | ---
    # |       |    |
    #  ------- ----

    if l2 == l3 and l1 + l2 == b1 and b2 + b3 == b1:
        print("YES")

    #  ------- ---- ---
    # |       |    |   |
    # |       |    |   |
    # |       |    |   |
    #  ------- ---- ---

    elif b1 == b2 == b3 and l1 + l2 + l3 == b1:
        print("YES")

    #  ------- 
    # |       |
    # |       |
    # |       |
    #  ------- 
    # |   |   |
    #  --- --- 

    elif b2 == b3 and b1 + b2 == l1 and l2 + l3 == l1: 
        print("YES")

    #  ------- 
    # |       |
    # |       |
    # |       |
    #  ------- 
    # |       |
    #  ------- 
    # |       |
    #  ------- 

    elif l1 == l2 == l3 and b1 + b2 + b3 == l1:
        print("YES")
    
    else:
        print("NO")
