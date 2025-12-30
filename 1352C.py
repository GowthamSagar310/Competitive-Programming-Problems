for _ in range(int(input())):
    n, k = map(int, input().split())
    # if k == 1:
    #     print(1)
    # else:
    #     # n1 = n-1
    #     # row = (k+n1-1) // n1
    #     # res = row * n
    #     # res -= n-(k % n1 if k % n1 != 0 else n1)
    #     # print(res)

    #     n1 = n-1
    #     row = (k+n1-1) // n1
    #     res = (row-1) * n
    #     res += k % n1 if k % n1 != 0 else n1
    #     print(res)

    # for every "n" numbers, (n-1) numbers are good and 1 is bad (divisible)
    # how many rows does it take to fill k numbers in (n-1) groups
    # 1   2  3  4
    # 5   6  7  8
    # 9  10 11 12
    # 13 14 15 16
    # n = 4, k = 10 (to fill 10 numbers in rows of length 3 = ceil(10 / 3) = 4)

    # row = ceil(k/n-1) = floor((k+n-1-1) / n-1)
    # how many multiples must be removed ? row-1
    # row-1 = floor((k+n-1-1-n+1)/n-1) = floor(k-1 / n-1)
    
    skips = (k-1) // (n-1)
    print(k + skips)