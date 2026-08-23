for _ in range(int(input())):
    n = int(input())
    
    """
    3 0, 1, 2
    5 0, 1, 2

    = 1
    1, 4, 7, 11, ...
    6, 11, 16, .....

    = 2 
    2, 5, 8, 11, ...
    2, 7, 12, 17, ...

    = 0
    3, 6, 9, 12, 15, ...
    5, 10, 15, ...

    n = 3k1 + 2 
    n = 5k2 + 2
    3k1 = 5k2

    3k1 + 2 <= n
    3k1 <= (n-2)
    for remainer = 2 -> k1 <= (n-2)//3
    k2 = (k1 / 5)
    """

    total = (n // 15)
    count = 3 * total
    if 15 * total + 0 <= n: count += 1
    if 15 * total + 1 <= n: count += 1
    if 15 * total + 2 <= n: count += 1
    print(count)