for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    w_count = 0
    minimum = float("inf")
    l = 0
    for r in range(n):
        if s[r] == "W":
            w_count += 1
        if r-l+1 == k:
            minimum = min(minimum, w_count)
            if s[l] == "W":
                w_count -= 1
            l += 1
    print(minimum)
