from math import log 
for _ in range(int(input())):
    n = int(input())

    total_sum = (n * (n + 1)) // 2

    # 1, 2, 4, ... x
    # x = 2 ^ k
    # 2 ^ k <= n
    # k <= log(n, 2)

    # sum of two powers = a (r ^ n - 1) // (r-1)
    # a = 1, r = 2
    # sum of two powers = 2 ^ (k+1) - 1

    k = int(log(n, 2))
    sum_of_two_powers = 2 ** (k+1) - 1
    print(total_sum - 2 * (sum_of_two_powers))