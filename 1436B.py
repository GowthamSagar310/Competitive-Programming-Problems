for _ in range(int(input())):
    n = int(input())

    """
    1. square should not contain prime numbers
    2. sum of each row and column must be prime

    0 1 4 6 8 9 

    sum should be prime
    meaning it should have divisors other 1 and itself.

    what if we can just have 0 and 1 ? 
    each row and columns should have two 1s, so the sum is always 2 (prime)
    """

    grid = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                grid[i][j] = 1
                grid[i][(j+1) % n] = 1
    
    for row in grid:
        print(*row)

