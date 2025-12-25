for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ones = arr.count(1)
    mini = ones % 2


    # 2 bulbs
    # 0 0 0 0 -> 0 max bulbs
    # 0 1 0 0 -> 1 max bulb
    # 1 1 0 0 -> 2 max bulbs
    # 1 1 1 0 -> cannot have 3 bulbs on, min(n, ones)

    # 3 bulbs
    # 0 0 0 0 0 0 -> 0 max bulbs
    # 0 1 0 0 0 0 -> 1 bulb
    # 0 1 1 0 0 0 -> 2
    # 1 1 1 0 0 0 -> 3
    # 1 1 1 1 0 0 -> 2
    

    # think of it like 
    
    # S S S
    # B B B 
    # S S S

    # switches on either side of bulb
    # if only lower are on, there count(1)
    # if upper row switches are on, they cancel lower
    # so go for remaing -> (2 * n) - ones -> count(0)


    maxi = ones if ones <= n else (2*n)-ones
    print(mini, maxi)
