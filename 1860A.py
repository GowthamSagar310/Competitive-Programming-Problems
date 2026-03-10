for _ in range(int(input())):
    s = input()
    n = len(s)

    pattern1 = "(" * n + ")" * n
    pattern2 = "()" * n

    if s == "()":
        print("NO")
    elif s not in pattern1:
        print("YES")
        print(pattern1)
    else:
        print("YES")
        print(pattern2)
    
    # the idea here is 
    # 1. if there are two consecutive equal characters in "s",
    #    i.e "((" or "))", it definitely wont be part in alternative string
    #    ()()()
    # 2. if there are no consecutive equal characters, then "s" must be 
    #    alternating like "()()", which wont be part of 
    #    regular bracket "(())", except for "()" which is a edge case
    # 3. "()" is part of every regular bracket string. 
