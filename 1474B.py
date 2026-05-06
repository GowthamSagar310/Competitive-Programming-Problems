def sieve():
    primes = [True] * (100001)
    primes[0] = primes[1] = False
    for i in range(2, 100001):
        if primes[i]:
            for j in range(i*i, 100001, i):
                primes[j] = False
    return primes
primes = sieve()

def get_next_prime(num):
    if primes[num]:
        return num
    for i in range(num+1, 100001):
        if primes[i]:
            return i

for _ in range(int(input())):
    d = int(input())

    """
    smallest positive integer 

    1. which has atleast 4 divisors
    2. difference between any two divisors is at least d

    1 = odd

    d = odd
    2+d = odd
    1+d+d = odd
    1+d+d+d = even

    d = even
    1+d = odd
    1+d+d = odd
    1+d+d+d = odd

    prime numbers
    1 = 1*2*3
    2 = 1*3*5
    3 = 1*5*
    """

    ans = 1
    next1 = get_next_prime(1+d)
    next2 = get_next_prime(next1+d)
    print(ans * next1 * next2)