for _ in range(int(input())):
    n, a, b = map(int, input().split())
    # if (abs(a-b)-1) & 1:
    #     print("YES")
    # else:
    #     print("NO")

    # the other way to code this is to see parity of a, b
    # if a and b are even, the number of tiles in between them -> odd
    # if a and b are odd, the number of tiles in between them -> odd
    # if a and b are of opp. parity, number of tiles between them -> even

    # if there are even tiles, alice is forced to move to 1 or n -> alice looses
    # if there are odd tiles, bob is forced to move 1 or n -> alice wins

    # check if parity is same or different.
    # (a xor b) & 1 = 0 -> same parity
    # (a xor b) & 1 = 1 -> different parity

    if (a^b) & 1:
        print("NO")
    else:
        print("YES")
