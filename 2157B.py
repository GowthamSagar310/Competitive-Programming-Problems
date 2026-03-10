for _ in range(int(input())):
    n, x, y = map(int, input().split())
    s = input()

    fours = s.count("4")

    if abs(x) > n or abs(y) > n: 
        print("NO")
    elif abs(x) <= n-fours:
        print("YES")
    else:
        # y should be with in range
        reduce_y = abs(x)-(n-fours)
        if abs(y) <= n-reduce_y:
            print("YES")
        else:
            print("NO")

    

