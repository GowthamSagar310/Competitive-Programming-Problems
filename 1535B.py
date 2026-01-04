from math import gcd
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr_s = sorted(arr, key=lambda x: x & 1)

    # to maximum the pairs, it is best to keep the even numbers at the start
    # because gcd(even, 2*(even|odd)) > 2
    # for odd numbers gcd(ai, 2*aj) is nothing but gcd(ai, aj)
    # because the 2 in the aj is one of the factor, which is not shared by ai because it is odd
    # for gcd(ai, aj) there is no pattern here, we just have to check all the pairs

    total = 0
    for i in range(n):
        for j in range(i+1, n):
            total += gcd(arr_s[i], 2 * arr_s[j]) > 1

    print(total)
