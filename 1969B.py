for _ in range(int(input())):
    s = input()
    """
    consecutive 1s + 1 zero
    """
    n = len(s)
    zeroes = ones = 0
    ops = 0
    # i = 0
    # while i < n:
    #     while i < n-1 and s[i] >= s[i+1]:
    #         if s[i] == "1": ones += 1
    #         else: zeroes += 1
    #         i += 1
    #     if i < n and s[i] == "0": zeroes += 1
    #     if zeroes and ones: ops += (ones + 1) * zeroes
    #     zeroes = 0
    #     i += 1
    # print(ops)

    for i in range(n):
        if s[i] == "1":
            ones += 1
        elif ones:
            ops += ones + 1
    print(ops)