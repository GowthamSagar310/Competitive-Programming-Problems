from math import isqrt
n, x = map(int, input().split())

"""
- max value of x is 10^9
- pairs of divisors

- find all the divisors of a number 
"""

def divisors(x, n):
    count = 0
    for i in range(1, isqrt(x)+1):
        if x % i == 0:
            if i <= n and (x // i) <= n:
                if i == x // i: count += 1
                else: count += 2
    return count
print(divisors(x, n))

