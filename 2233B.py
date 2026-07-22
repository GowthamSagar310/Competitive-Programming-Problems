for _ in range(int(input())):
    n = int(input())

    """
    n = 2
    2 1 1 2 1 2 2 1 

    n = 3
    3 2 1 1 3 2 1 3 2 3 2 1
    
    n = 4
    4 3 2 1 1 4 3 2 1 4 3 2 4 3 2 1
    
    n = 5
    [5 4 3 2] 1 1 [5 4 3 2] 1 [5 4 3 2] [5 4 3 2] 1
    """

    block = list(range(n, 1, -1))
    ans = block + [1, 1] + block + [1] + block + block + [1]
    print(*ans)

