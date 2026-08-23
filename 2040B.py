for _ in range(int(input())):
    n = int(input())
    """
    al ... + ar = ceil(length of substring / 2)

    10010000000000000000 op1=2
    11110000000000000000 op1=2
    11110000010000000000 op1=3
    11111111110000000000 op1=3
    11111111110000000001 op1=4
    11111111111111111111 op1=4

    op = 1
    x = 1 -> (x+1) * 2 = 4 op += 1
    x = 4 -> (x+1) * 2 = 10 op += 1
    x = 10 ->          = 22 op += 1


    """
    x = 1
    ops = 1
    while x < n:
        x = (x+1) * 2
        ops += 1
    print(ops)
    
    


