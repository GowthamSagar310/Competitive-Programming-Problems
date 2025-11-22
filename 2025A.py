for _ in range(int(input())):
    s = input()
    t = input()
    ops = 0
    prefix = 0
    for l1, l2 in zip(s, t):
        if l1 == l2:
            prefix += 1
        else:
            break
    ops = prefix + 1 if prefix else 0
    print(ops + len(s) + len(t) - 2 * prefix)