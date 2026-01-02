for _ in range(int(input())):
    x, n = map(int, input().split())
    
    """
    start at even
    n = 1      0-1        -1       displacement=-1 (from 0 to -1) -> -1
    n = 2     -1+2        +1       displacement=+1 (from 0 to +1) -> +1
    n = 3      1+3        +4       displacement=+4 (from 0 to +4) -> n+1
    n = 4      4-4         0       displacement=0 (from 0 to 0) -> 0
    cycle repeats
    
    start at odd
    n = 1      1+1         2       displacement=1 (from 1 to 2) -> +1
    n = 2      2-2         0       displacement=-1 (from 1 to 0) -> -1
    n = 3      0-3        -3       displacement=-3 (from 1 to +4) -> -(n+1)
    n = 4      -3+4        1       displacement=0 (from 1 to 1) -> 0
    cycle repeats
    """

    remainder = n % 4
    if remainder == 0: displacement = 0
    elif remainder == 1: displacement = -n
    elif remainder == 2: displacement = 1
    elif remainder == 3: displacement = n+1

    if x % 2 == 0:
        print(x + displacement)
    else:
        print(x - displacement)

    
