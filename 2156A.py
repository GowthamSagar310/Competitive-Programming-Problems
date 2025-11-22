for _ in range(int(input())):
    n = int(input())

    # m1 + m2 + m3 
    # minimize m1 and m2 
    # m1 = 1
    # m2 = 1 
    # m3 = m-2
    # m-2 gets carried over, in which hao might have a change to eat a slice
    # we just have to maximize count, not amount

    # 8 can be visualized as 
    # 1 1 [6]
    #     1 1 [4]
    #         [1 1 2]
    # [1 1 1 1 1 1 2]
    #  --- --- --- -
    # (number of pairs of 2) - 1
    # last is anyway eaten by alex

    # 8 -> 1 1 1 1 1 1 [2] 4-1
    # 7 -> 1 1 1 1 1 1 [1] 4-1

    # if n % 2 == 0:
    #     print((n // 2) - 1)
    # else:
    #     print((n-1) // 2)
    
    # (n + 1) // 2 is just a trick to make it work without if statements
    print(((n+1)// 2)-1)