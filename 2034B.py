for _ in range(int(input())):
    n, m, k = map(int, input().split())
    s = input()
    count = 0
    i = 0
    ops = 0
    while i < n:
        if s[i] == "0":
            count += 1
            if count == m:
                # start from i, min(i+k, n-1)
                # we can mark all of the items as 1
                # so "i" can jump to i+k
                i += k
                ops += 1
                count = 0
                continue
        else:
            count = 0
        i += 1
    print(ops)