# def solve(arr):
#     primes = [
#         3, 5, 7,
#         11, 13, 17, 19,
#         23, 29,
#         31, 37,
#         41, 43, 47,
#         53, 59,
#         61, 67,
#         71, 73, 79,
#         83, 89,
#         97
#     ]
#     mini = float("inf")
#     for num in arr:
#         if num % 2 == 1:
#             # if the number is odd, then 2 is the minimum possible x
#             return 2 
#         else:
#             # if the number is even, gcd(2, even) = 2 != 1, so 2 cannot be the answer
#             # we have to find minimum possible number for which atleast one of the numbers, gcd(x, num) = 1
#             # so x has to be a prime number and x should not divide the number
#             # in other way, we are just looking for the smallest prime number which is not present in the prime factorization of this number
            
#             # but how many prime numbers to check for ? 
#             # given constraints: 2 <= x <= 10^18
#             # should we check for all the primes < 10^18 ? NO 
#             # because, 
#             # 1. if there is a number like 1011 = 3 * 337
#             # there is 5 missing from this number, so we will surely catch 5. 
#             # 2. but what if all the primes (< 100) are present ? 
#             # meaning, number = 3 * 5 * 7 * 11 * .... 97 = this pretty surely crosses 10^18 (which is not possible according to the question)
#             # so, in this scenario it is just -1 

#             # so if some prime is not present, we will catch it.
#             # but all of these are present, then surely it is -1

#             # it is actually sufficient to check till 53 because 
#             # 3 * 5 * 7 ... 53 > 10^18
#             for p in primes:
#                 if num % p:
#                     mini = min(mini, p)
#                     break
#     return mini if mini != float("inf") else -1

# for _ in range(int(input())):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     print(solve(arr))

def solve(arr):
    primes = [
        2, 3, 5, 7,
        11, 13, 17, 19,
        23, 29,
        31, 37,
        41, 43, 47,
        53, 59,
        61, 67,
        71, 73, 79,
        83, 89,
        97
    ]
    mini = float("inf")
    for num in arr:
        # if the number is odd, gcd(2, odd) = 1 -> 2 is the smallest possible.
        # if the number is even, gcd(2, even) = 2 != 1, so 2 cannot be the answer
        # we have to find minimum possible number for which atleast one of the numbers, gcd(x, num) = 1
        # so x has to be a prime number and x should not divide the number
        # in other way, we are just looking for the smallest prime number which is not present in the prime factorization of this number
        
        # but how many prime numbers to check for ? 
        # given constraints: 2 <= x <= 10^18
        # should we check for all the primes < 10^18 ? NO 
        # because, 
        # 1. if there is a number like 1011 = 3 * 337
        # there is 5 missing from this number, so we will surely catch 5. 
        # 2. but what if all the primes (< 100) are present ? 
        # meaning, number = 3 * 5 * 7 * 11 * .... 97 = this pretty surely crosses 10^18 (which is not possible according to the question)
        # so, in this scenario it is just -1 

        # so if some prime is not present, we will catch it.
        # but all of these are present, then surely it is -1

        # it is actually sufficient to check till 53 because 
        # 2 * 3 * 5 * 7 ... 53 > 10^18
        for p in primes:
            if num % p:
                mini = min(mini, p)
                break
    return mini if mini != float("inf") else -1

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr))


# if there is atleast one odd number in the array, answer must be 2 as gcd(2, odd) = 1
# if every number in the array is even, then we must find the smallest odd number (to have gcd as 1). for every composite odd number, there is always a smaller prime number which also gives gcd as 1. so it comes down to finding the smallest prime number.
# how many prime numbers to check for ? primes number < 100 are enough because
# if the number is missing a prime (<100), then that is the answer.
# but if it is not missing any prime (2 * 3 * 5 .. 97), then number is way greater than 10^18, which is not possible because of the constraint.
# till 53 is enough to check but instead of calculating the above value, we can look at numbers which contain 10, and there are more than 18 numbers in primes (<100) which have 10 in them, so multiplying them would give > 10^18.

# why not odd numbers ? why are we only checking for primes ?
# say, there exists a composite number C which is the answer
# if C >= 2, then there must exist atleast one prime factor
# C = p * k (prime factorization by fundamental theorem of arithmetic)
# gcd(Ai, C) = 1
# 1. p is a factor of C
# 2. Ai and C have no common factors 
# therefore, p cannot be a factor inside Ai. gcd(Ai, p) = 1
# Since C = p * k, meaning k >= 1 and p < C
# we found a prime p, which is smaller than the composite C. 
# so there exists a prime always which is smaller than the odd composite.