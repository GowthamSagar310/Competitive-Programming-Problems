for _ in range(int(input())):
    a, b, c = map(int, input().split())

    # dumber bitwise solution
    # if (a ^ b) != 0:
    #     if (a ^ c) != 0: print(a)
    #     else: print(b)

    # elif (b ^ c) != 0:
    #     if (b ^ a) != 0: print(b)
    #     else: print(c)

    # elif (c ^ a) != 0:
    #     if (a ^ b) != 0: print(c)
    #     else: print(a)

    # we can just take xor of all three numbers 
    
    print(a ^ b ^ c)
