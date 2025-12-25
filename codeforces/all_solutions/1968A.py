for _ in range(int(input())):
    x = int(input())

    # 1 <= y < x
    # gcd(x, y) + y should be maximum

    # divisors of 10 -> 1 2 5 10
    # gcd(x, y) + y
    # gcd(10, 10-1) + 9
    # 10

    # gcd(21, 21-1) + 20 = 1 + 20 = 21
    # gcd(21, 18) + 18 = 3 + 18 = 21
    
    print(x-1)

    # formal proof
    # gcd(x, y) + y
    # gcd(x-y, y) + y
    # gcd(x-y, y) <= x-y
    # gcd(x-y, y) + y <= x-y+y
    # gcd(x, y) + y <= x
    # the upper bound is <= x

    # 1 <= y < x
    # maximum value of y = x-1
    # gcd(x, x-1) + x-1 = x 
    # this is the maximum value that we proved above.

 