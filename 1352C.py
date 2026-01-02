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

    # q: if I skip few numbers and end up multiple of n ? 
    #    meaning what if (k+skips) % n == 0
    #    is this ever possible ? 

    # take (k-1)/(n-1)
    # k-1 = q(n-1) + r
    # so -> 0 <= r < n-1

    # answer = k + floor(k-1/n-1)
    # answer = k + q
    # answer = q(n-1) + r + 1 + q
    # answer = qn + r + 1
    
    # answer % n = r + 1
    # from about we know that 0 <= r < n-1
    # 1 <= r + 1 < n
    # so r + 1 is never zero and we are never going to fall on divisible number