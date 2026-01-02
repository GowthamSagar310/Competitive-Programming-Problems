n = int(input())

primes = [True] * (n+1)
primes[0] = primes[1] = False
for i in range(2, n+1):
    if primes[i]:
        for j in range(i*i, n+1, i):
            primes[j] = False

def get_count(n):
    count = 0
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            if primes[i]:
                count += 1
            if i * i != n:
                if primes[(n//i)]:
                    count += 1
    return count

count = 0 
for i in range(3, n+1):
    if get_count(i) == 2:
        count += 1
print(count)
