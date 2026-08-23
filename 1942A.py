for _ in range(int(input())):
    n, k = map(int, input().split())
    if k == 1:
        print(*list(range(1, n+1)))
    elif n == k:
        print(*[1] * k)
    else:
        print(-1)
