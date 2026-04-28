for _ in range(int(input())):
    n = int(input())


    """
    
    after the first B, there are no A / N at all (which ever is minimum), then no subsequence

    n = 1 BAN, NAB 1
    n = 2 BANBAN, NANBAB  1
    n = 3 2
    
    n = 4 2
    BAN BAN BAN BAN
    NAN NAN BAB BAB

    n = 5
    
    1                 15
    BAN BAN BAN BAN BAN
    NAN NAN BAN BAB BAB

    1 15
    4 12


    """

    ops = (n+1) // 2
    print(ops)

    i = 0
    for _ in range(ops):
        print(i+1, (3 * n)-1-i+1)
        i += 3