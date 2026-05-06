for _ in range(int(input())):
    a, b = map(int, input().split())

    # mex is equal to a
    # so all the values from 0 to a-1 should be present

    # TLE
    # xor = 0
    # for i in range(0, a):
    #     xor ^= i

    # there is a trick to calculate the xor value from 0 ^ 1 ^ 2 ..^ n
    # 4k   = ....00
    # 4k+1 = ....01
    # 4k+2 = ....10
    # 4k+3 = ....11
    # xor of all these = 0
    # 4k ^ (4k+1) ^ (4k+2) ^ (4k+3) = 0
    # for k = 0, (0 ^ 1 ^ 2 ^ 3) = 0
    # for k = 1, (4 ^ 5 ^ 6 ^ 7) = 0
    # .
    # .

    # if blocks of 4 are gone, only incomplete blocks are remaining
    # OBSERVE THAT THE BLOCK IS START FROM 0. NOT 1. 

    # case n % 4 == 0
    # (0, 1, 2, 3) (4, 5, 6, 7) (....) will be zero
    # last n (which is divisible by 0) will be left
    # xor (0 .... n) = n

    # case n % 4 == 1
    # first two elements in the block are present (because the second element gives remainder 1)
    # (4k) ^ (4k+1) = 1
    # xor (0 .... n) = 1

    # case n % 4 == 2
    # (4k) ^ (4k+1) ^ (4k+2)
    # 1 ^ (4k+2) = 4k+3
    # in the last block, there are only three values.
    # 4k+2 will be n
    # so 4k+3 = n+1

    # case n % 4 == 3
    # all values present in the last block, so 0

    def get_xor(n):
        if n % 4 == 0: return n
        if n % 4 == 1: return 1
        if n % 4 == 2: return n+1
        return 0

    xor = get_xor(a-1)
    if xor == b:
        print(a)
    else:
        x = xor ^ b
        if x == a:
            print(a+2)
        else:
            print(a+1)
