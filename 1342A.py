for _ in range(int(input())):
    x, y = map(int, input().split())
    a, b = map(int, input().split())

    if  2 * a <= b:
        # use all a's
        print((x + y) * a)
    else:
        x, y = min(x, y), max(x, y)
        print(x * b + (y-x) * a)

