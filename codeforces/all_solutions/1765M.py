from math import isqrt

for _ in range(int(input())):
    n = int(input())

    # a + b = n
    # lcm(a, b) should be minimum 
    # l = (a * b) // g

    # as g increases, l decreases
    # g <= min(a, b)
    # g is minimum if a is more and b is multiple of a

    # a + k.a = n
    # a.(1+k) = n
    # a = n // (1+k)

    # a, b, n are integers 
    # so n // (1+k) should be an integer

    # a > 0 and b > 0
    # k != 0

    # l = a * k * a / gcd(a, ka)
    # l = k * a
    # minimize k -> minimize the divisor of n as n % (1+k) == 0
    # 1+k = d = first divisor of n

    # brute force
    # for i in range(1, n):
    #     if n % (1 + i) == 0:
    #         a = n // (1 + i)
    #         b = i * a
    #         print(a, b)
    #         break


    # divisors here are other than 1 and n
    # because there are our last option.
    # divisors = []
    # for i in range(2, isqrt(n)+1):
    #     if n % i == 0:
    #         divisors.append(i)
    #         if i * i != n:
    #             divisors.append(n // i)
    
    # if not divisors:
    #     print(1, n-1)
    # else:
    #     a = n // divisors[0]
    #     b = n-a
    #     print(a, b)

    # we can just choose first divisor
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            a = n // i
            b = n - a 
            print(a, b)
            break
    else:
        print(1, n-1)