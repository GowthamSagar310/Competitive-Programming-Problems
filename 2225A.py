for _ in range(int(input())):
    x, y = map(int, input().split())


    """
    
    y > x 
    y % x == 0

    i need to find x < z < y (not equal)
    z % x == 0 but y % z != 0
    
    z = x+k (k > 0)
    (x+k) % x == 0
    k should be divisible by x
    z = 2x, 3x .....

    y % x == 0
    
    y = k1 * x
    z = k2 * x
    
    y % z != 0
    k2 does not divide k1

    k1 = y // x
    k2 in [2, 3, 4, 5 ... k1-1]

    1234567890 12345678900
    k1 = y // x = 10
    k2 can be k1-1 = 9

    1234567890 1234567890*9 12345678900

    
    
    """

    if y == 2 or (y // x) == 2:
        print("NO")
    else:
        print("YES")
