for _ in range(int(input())):
    a, b = map(int, input().split())

    # a ^ x + b ^ x 
    # this value should be minimum

    # if one part of the expression is not present, can we get the smallest ? 
    # if x = a, a ^ x = 0 and b ^ x = b ^ x
    # optimally, to mimize, we need to have same bits set in a/b and x
    
    
    print(a ^ b)
    