for _ in range(int(input())):
    x, y, z = map(int, input().split())

    # a & b = x
    # b & c = y
    # c & a = z

    # 3 = 011
    # 2 = 010
    # 6 = 110

    # between x, y -> if there are same set of bits, that can be b
