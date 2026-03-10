for _ in range(int(input())):
    x, y = map(int, input().split())

    """
    x > y 
    diff = x-y
    """

    diff=x-y
    print("YES" if diff != 1 else "NO")