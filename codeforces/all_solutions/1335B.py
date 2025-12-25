for _ in range(int(input())):
    n, a, b = map(int, input().split())
    alpha = "abcdefghijklmnopqrstuvwxyz"
    res = list(alpha[:b])
    l = 0
    r = b
    while r < n:
        res.append(res[l])
        l += 1
        r += 1
    print("".join(res))