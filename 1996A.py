for _ in range(int(input())):
    n = int(input())

    # count = 0
    # count += (n // 4)
    # n = n % 4
    # count += (n // 2)
    # print(count)

    # other solution is
    # if n % 4 == 0, then n // 4 cows + 0 chicken
    # if n % 4 != 0, then must be atleast 1 chicken
    # so (n-2) // 4 cows + 1 chicken
    # (n-2) // 4 must be divisible if farmer counts properly
    # this is minimum possible combination (not reality)

    # print(((n - 2) // 4) + (1))
    print((n + 2) // 4)
    