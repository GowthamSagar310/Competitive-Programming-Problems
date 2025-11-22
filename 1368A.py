for _ in range(int(input())):
    a, b, n = map(int, input().split())

    # this forms a kind of fibonacci sequence
    # the worst use case is a = 1, b = 1 and n = 10^9
    # ~ log(n) ~ 43 steps
    # so just brute force.

    ops = 0
    while a <= n and b <= n:
        a, b = max(a, b), min(a, b)
        b += a
        ops += 1
    print(ops)
