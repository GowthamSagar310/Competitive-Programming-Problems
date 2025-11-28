for _ in range(int(input())):
    a, b = map(int, input().split())

    # a ^ x + b ^ x 
    # this value should be minimum

    # if one part of the expression is not present, can we get the smallest ? 
    # if x = a, a ^ x = 0 and b ^ x = b ^ x
    # optimally, to mimize, we need to have same bits set in a/b and x
    

    # ideally we want the smallest value to be 0
    # for each individual bit, we need to see what is the smallest value possible

    # if a and b have same bits at position i
    # to minimize, a ^ x + b ^ x
    # x can be 0 if a = b = 0 -> 0 ^ 0 + 0 ^ 0 = 0
    # x can be 1 if a = b = 1 -> 1 ^ 1 + 1 ^ 1 = 0
    # so this bit in x should a ^ b

    # if a and b have different bits at position i
    # a = 0, b = 1 -> 0 ^ 0 + 1 ^ 0 = 1
    # a = 1, b = 0 -> 1 ^ 0 + 0 ^ 0 = 1
    # no matter what minimum value is 1 if a and b have different bits
    # which is also property of xor 
    
    print(a ^ b)
    