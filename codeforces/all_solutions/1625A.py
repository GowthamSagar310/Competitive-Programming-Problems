results = [17, 18, 1, 1, 39, 0, 2]
for j in range(int(input())):
    n, l = map(int, input().split())
    arr = list(map(int, input().split()))


    # we need to minimize the distance
    # distance(x, y) = how many positions have different bits
    # 
    # how to quickly know if two bits are different ? bit1 ^ bit2 will be 1
    # so, (total number of bits in x ^ y)
    # 
    # we need to do this for all the numbers
    # for each number
    #      total number of bits in x ^ y 
    # should be minimized 
    # or we can reverse this and say
    # for each bit
    #      for each number in xi ^ yi (i -> bit position)

    # so, for a position "i", over all the numbers
    # say, there are 5 numbers which have this "i" position set and 3 which dont
    # observe that 5 + 3 = 8 (say n)
    # if i choose to not set this bit in y, the distance is going to be 5
    # if i set this bit however, the distance is going to be only 3
    # like wise we minimise the distance over each bit 
    # and this is independent, setting a bit somewhere else is not going to change this one
    # or the distance that this bit produces over all the numbers

    bit_freq = [0] * 32
    for a in arr:
        for i in range(32):
            if a & (1 << i):
                bit_freq[i] += 1
    
    res = 0
    for i in range(32):
        one_count = bit_freq[i]
        zero_count = n - one_count
        if one_count > zero_count:
            res = res | (1 << i)
    print(res)