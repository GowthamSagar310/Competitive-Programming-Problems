for _ in range(int(input())):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    curr_max = max(arr)
    ans = []
    for _ in range(q):
        s, l, r = input().split()
        l, r = int(l), int(r)
        if s == "+" and l <= curr_max <= r:
            curr_max += 1
        elif s == "-" and l <= curr_max <= r:
            curr_max -= 1
        ans.append(curr_max)
    print(*ans)

