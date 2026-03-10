for _ in range(int(input())):
    
    n, k = map(int, input().split())

    # TLE
    # count = 0
    # while n != 0:
    #     if n % k == 0: n //= k
    #     else: n -= 1
    #     count += 1
    # print(count)

    count = 0
    while n != 0:
        q, r = divmod(n, k)
        if n % k == 0: 
            n = q
            count += 1
        else: 
            n -= r
            count += r
    print(count)