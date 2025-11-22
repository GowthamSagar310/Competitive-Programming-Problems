# from math import isqrt
# for _ in range(int(input())):
#     n = int(input())
#     r = isqrt(n)
#     if r * r == n:
#         # a + b = r
#         # a >= 0
#         # b >= 0
#         # a = 0
#         # b = r
#         print(0, r)
#     else:
#         print(-1)

# this problem is tagged as binary search because 
# we can find the square root using binary search

def perfect_square(n):

    # x <= 9999
    # x ~ 10000
    # sqrt(x) ~ 100

    l = 0
    r = 100
    while l <= r:
        mid = (l + r) >> 1
        sq = mid * mid
        if sq == n:
            return mid
        elif sq < n:
            l = mid+1
        else:
            r = mid-1
    return -1 # not perfect square

for _ in range(int(input())):
    n = int(input())
    r = perfect_square(n)
    if r != -1:
        # a + b = r
        # a >= 0
        # b >= 0
        # a = 0
        # b = r
        print(0, r)
    else:
        print(-1)



