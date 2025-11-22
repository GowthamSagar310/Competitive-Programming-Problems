for _ in range(int(input())):
    n = int(input())

    # a + b + c = n
    # gcd(a, b) = c
    # a % c = 0
    # b % c = 0

    if n % 2 == 0:
        print((n // 2)-1, n // 2, 1)
    else:
        pass