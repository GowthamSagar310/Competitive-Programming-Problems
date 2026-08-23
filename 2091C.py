for _ in range(int(input())):
    n = int(input())

    """
    5 4 3 2 1

    1 3 2 
    2 1 3
    3 2 1
    1 3 2

    1 2 3 4 5 6 7
    7 6 5 4 3 2 1
    1 7 6 5 4 3 2
    2 1 7 6 5 4 3
    3 2 1 7 6 5 4
    4 3 2 1 7 6 5
    5 4 3 2 1 7 6

    """

    if n % 2 == 0:
        print(-1)
    else:
        print(*list(range(n, 0, -1)))