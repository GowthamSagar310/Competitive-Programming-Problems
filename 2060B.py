for _ in range(int(input())):
    n, m = map(int, input().split())
    cows = []
    for i in range(n):
        cards = sorted(list(map(int, input().split())))
        cows.append((i+1, cards))
    cows.sort(key=lambda x: x[1][0])
    possible = True
    prev = -1
    for j in range(m):
        for i in range(n):
            if cows[i][1][j] < prev:
                possible = False
                break
            prev = cows[i][1][j]
    if possible:
        print(*[cows[i][0] for i in range(n)])
    else:
        print(-1)