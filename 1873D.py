for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    i = 0
    ops = 0
    while i < n:
        if s[i] == "B":
            ops += 1
            i += k
        else:
            i += 1
    print(ops)