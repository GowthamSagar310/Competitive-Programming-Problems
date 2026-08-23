for _ in range(int(input())):
    n = int(input())
    """
    0 =  000000000
    1 =  000000001
    2 =  000000010
    3 =  000000011
    4 =  000000100
    5 =  000000101
    6 =  000000110
    7 =  000000111
    8 =  000001000
    9 =  000001001

    nums with 0th bit set = (1, 3, 5, 7, 9)
    nums with 1st bit set = (2, 3, 6, 7)
    nums with 2nd bit set = (4, 5, 6, 7)
    nums with 3rd bit set = (8, 9)
    
    we need to find the permuation which has = max(adjacent pair's xor)
    """
    n -= 1
    max_bit_set = 0
    for i in range(31, -1, -1):
        if n & (1 << i):
            max_bit_set = i
            break

    

    


    ans = []
    while n > 0 and n & (1 << max_bit_set):
        ans.append(n)
        n -= 1
    ans.append(0)
    ans.extend(list(range(n, 0, -1)))
    print(*ans)