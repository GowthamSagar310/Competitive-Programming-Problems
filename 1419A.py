for _ in range(int(input())):
    n = int(input())
    num = input()
    ro, be = 0, 0
    for i in range(n):
        d = int(num[i])
        index = i+1
        if index & 1:
            if d & 1:
                ro += 1
        else:
            if d % 2 == 0:
                be += 1

    if n & 1:
        # breach would complete his turn and there would be only one digit left.
        # can the last digit be O? meaning raze removed all his even values
        if ro > 0:
            print(1)
        else:
            print(2)
    else:
        if be > 0:
            print(2)
        else:
            print(1)

    """
    raze starts. 
    if n is odd, the last turn would be of raze. so if there is odd number, raze would win. 
    if n is even, the last turn would be of breach. so if there is even number, breach would win. 
    """