from math import lcm
for _ in range(int(input())):
    a, b = map(int, input().split())

    # m = k1.a + r
    # m = k2.b + r
    # m >= a or m >= b or m >= a,b
    # smallest m value ? 

    # to give the same remainder
    # the number should be greater than both a and b ? 
    # if a == b, m = a
    # if a != b, (a * b) // gcd(a,b)

    # m-r should be divisible by both a, b 
    # that means m-r is a common multiple of a, b
    # let the LCM(a,b) = L
    # m-r = k * L
    # meaning, if m-r is divisible by a, b
    # if it will be in some form of k * L
    # 
    # now to minimize it,
    # we can say r = 0 and k = 1
    # m = L -> lcm(a,b)
    # 
    # how do we prove that there is no number m1 < L ? 
    # 
    # m1 - r is divisible by both a, b
    # m1 - r is divisible by L
    # but also m1 < L -> m1 - r < L but this is contradicting
    # 
    # m1 = r + k * L 
    # m1 < L
    # means that k = 0
    # m1 = r
    # if m1 = r = remainder should be less that a, b
    # m1 = r < min(a, b)
    # which is a violation of the constraint

    # print((a * b) // gcd(a, b))
    print(lcm(a, b))