for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    # length of the sequence is just hundred n = 100
    # A and B <= min(A, B)
    # I can never set an extra bit. 
    # 
    # now, it is all about removing the set bit. 
    # if 3rd number contains 0 at 3rd bit, and rest all contains 1
    # i can set the 3rd bit in the final answer as zero
    # with the given operations

    # so if there is unset bit at a pos in some number
    # final answer will also have unset bit at pos

    # this means, I can AND all numbers and see what is left over
    # (left over bits are set bits in all the numbers, can never be remomved)

    res = arr[0]
    for i in range(1, n): res &= arr[i]
    print(res)