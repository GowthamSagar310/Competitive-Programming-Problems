for _ in range(int(input())):
    n = int(input())
    s = input()

    # if map -> remove a
    # if pie -> remove i
    # if mapie -> remove p
    
    cost = 0
    i = 0
    while i < n:
        next_five = s[i:i+5]
        next_three = s[i:i+3]
        if next_five == "mapie":
            # remove p
            cost += 1
            i += 5
        elif next_three == "map":
            cost += 1
            i += 3
        elif next_three == "pie":
            cost += 1
            i += 3
        else:
            i += 1
    
    print(cost)