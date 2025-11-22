from math import isqrt
n = int(input())

def get_divisors(n):
    divisors = []
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            divisors.append((i, n // i))
    return divisors

divisors = get_divisors(n)
print(divisors[-1][0], divisors[-1][1])