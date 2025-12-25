# def solve(n):
#     ops = 0
#     while n != 1:
#         if n % 6 == 0:
#             n //= 6
#             ops += 1
#         else:
#             if (2 * n) % 6 == 0:
#                 n *= 2
#                 ops += 1
#             else:
#                 return -1
#     return ops if n == 1 else -1

def solve2(n):

    ops = -1
    count_2 = count_3 = 0
    while n % 2 == 0:
        n //= 2
        count_2 += 1
    
    while n % 3 == 0:
        n //= 3
        count_3 += 1
    
    # 1. if there are prime factors other than [2, 3] they cannot be cancelled
    # 2. if there are more 2's in prime factorization, we cannot eliminate them
    # 3. if there are more 3's in prime factorization, we can add 2's and divide by 6 to eliminate one 2 and one 3

    # after removing all 2, 3's there should be only 1
    if n == 1 and count_2 <= count_3:
        # ops = add remaining 2's + eliminate all 3's
        ops = ( count_3 - count_2 ) + count_3
    
    return ops

for _ in range(int(input())):
    n = int(input())
    print(solve2(n))