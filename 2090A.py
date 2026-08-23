for _ in range(int(input())):
    x, y, a = map(int, input().split())
    a += 0.5
    """
    - per two days, they will dig x+y meters
    - a / (x+y) * (2 days)
    """

    k = a // (x + y)
    a -= k * (x + y)
    if x >= a:
        print("NO")
    else:
        print("YES")