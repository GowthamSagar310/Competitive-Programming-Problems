for _ in range(int(input())):
    n, m = map(int, input().split())

    # m columns
    
    # we want to maximize horizontal bricks
    # so, we want more number of horizontal bricks, that is less k
    # we can think of place as many 1x2 bricks
    # 

    # 7 rows, 8 columns
    # 8 % 2 == 0
    # 7 * (8 // 2)

    # 16 rows, 9 columns
    # 9 % 2 == 1
    # (9 // 2)-1 = 3
    # 3 * (1x2 bricks) + (1x3 brick)
    # 4 * 16 = 64

    # stability = horizontal bricks - vertical bricks
    
    print(n * (m // 2))