import math
for _ in range(int(input())):
    n = int(input())

    # n = a + b + c + d
    # 
    # a is nearly prime if a = p * q
    # p and q are primes, 1 < p < q
    # 
    # a, b, c, d are different and positive integers
    # these cannot be prime numbers
    # 
    # atleast three of them are nearly prime, the remaining can be anything.

    if n <= 6 + 10 + 14:
        print("NO")
    else:
        print("YES")
        d = n-30
        if (d == 6 or d == 10 or d == 14):
            print(6, 10, 15, n-31, sep=" ")
        else:
            print(6, 10, 14, n-30, sep=" ")