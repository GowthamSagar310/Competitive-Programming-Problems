n = int(input())

# sieve 
# primes = [True] * (n+1)
# primes[0] = primes[1] = False

# for i in range(2, n+1):
#     if primes[i]:
#         for j in range(i**2, n+1, i):
#             primes[j] = False

# i = 2
# while n-i >= 0:
#     if not primes[n-i] and not primes[i]:
#         print(i, n-i)
#         break
#     i += 1


# n >= 12
# 
# if n is even, 
# 4 is even and composite, n-4 is even and >= 8, which have 2 as a factor
# 4, n-4 is one valid combination
# 
# if n is odd,
# 9 is odd and composite, n-9 is even and >= 3, which have 2 as a factor
# 9.  n-9 is one valid combination

if n & 1:
    print(9, n-9)
else:
    print(4, n-4)