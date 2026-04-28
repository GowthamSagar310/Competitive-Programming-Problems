for _ in range(int(input())):
    x, y = map(int, input().split())

    """
    k = 0 

    op1: k = k + 1
    op2: k = k + x * 10 ^ p (for p >= 0)
    
    minimum number of ops to make k = y

    1. at each stage look at the biggest value of k that can be made using op2 can be used.
    """

    k = 0
    ops = 0
    while k != y:
        p = 0
        while k + x * (10 ** p) <= y:
            p += 1
        if p == 0:
            # cannot use x anymore. 
            ops += y-k
            break
        else:
            # able to increase the power to p-1 (not p because the loop broke when the power was p)
            k = k + x * (10 ** (p-1))
            ops += 1
    print(ops)

    # another way to solve. 

    # 1. how many of x's can fit in y ? 
    # q = y // x
    # r = y % x

    # q is nothing but a1 * 10^p1 + a2 ^ 10^p2 + ... 
    # q = a1 ops with p1 + a2 ops with p2 + ...
    # 
    # r must be filled with only k + 1 (op1)

    # ops = (digits of q) + r