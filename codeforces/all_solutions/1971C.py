for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    
    # think of a-b line
    # if c-d has to cross, c and d should be on opposite sides of a-b
    # if touch to a / b, it can be considered as opposite

    # a_to_b = []
    # i = a
    # while i != b:
    #     a_to_b.append(i % 12 if i != 12 else 12)
    #     i = (i % 12) + 1
    # a_to_b.append(b)

    # b_to_a = []
    # i = b
    # while i != a:
    #     b_to_a.append(i % 12 if i != 12 else 12)
    #     i = (i % 12) + 1
    # b_to_a.append(a)

    # if (c in a_to_b and d in b_to_a) or (c in b_to_a and d in a_to_b):
    #     print("YES")
    # else:
    #     print("NO")
    


    # Shorter solution - clever idea

    # start from 1 and go till 12
    # if two blue points are consecutive, that means lines never intersect
    # same for red 

    s = ""
    for i in range(1, 13):  
        if i == a or i == b: s += "b"
        if i == c or i == d: s += "r"
    
    print("YES" if s == "brbr" or s == "rbrb" else "NO")
