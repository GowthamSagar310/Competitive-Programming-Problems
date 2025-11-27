for _ in range(int(input())):
    x = int(input())

    # find b, such that a & b > 0
    # meaning atleast on common bit, say the last set bit of a, to minimize b

    # find b, such that a ^ b > 0
    # meaning atleast on different bit

    # 1. set the least significant set bit in a also in b -> AND part
    # 2. toggle the least significant bit, which is not processed above


    # a = 0100100
    # b = 0000100
    # b = 0000101

    # a = 0100101
    # b = 0000001
    # b = 0000011


    # if there is only single bit in x
    # we need have one more extra bit else we can just set the last set bit in a

    y = 0
    if x & (x-1):
        # there are more than 1 set bit in a
        # so, last bit in a -> set in b
        # this is enough, because, a ^ b will be > 0 as there are other bits
        y = y | (x ^ x & (x-1))
    else:
        # there is only one set bit in a
        if x & 1:
            y = 3
        else:
            y = x + 1
    print(y)
    