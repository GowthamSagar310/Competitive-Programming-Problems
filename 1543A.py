for _ in range(int(input())):
    a, b = map(int, input().split())

    # gcd(a, b) <= min(a, b)
    # op1: a+1, b+1
    # op2: a-1, b-1

    # difference between a, b is not going to change
    # a-b is not changing
    # gcd(a, b) = gcd(a-b, b) = gcd(a-b, a)
    
    if a == b: print(f"{0} {0}"); continue
    d = abs(a-b)
    m = max(a, b)
    
    # gcd(d, m) <= max(d, m)
    # d <= m
    # gcd(d, m) <= d
    # so the maximum value of gcd(a, b) is d
    # since the maximum value is d, I need to make the bigger number (>d)
    # divisible by d. for that I need to check the remainder

    # gcd(a,b) = gcd(d, m)
    # m > d
    
    # 8 % 6 = 2 (better to remove 2 than add 4)
    # 9 % 6 = 3
    
    r = m % d
    print(f"{d} {min(r, d-r)}")