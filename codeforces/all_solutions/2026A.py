for _ in range(int(input())):
    x, y, k = map(int, input().split())
    x = y = min(x, y)

    print(0, 0, x, y)
    print(0, y, x, 0)