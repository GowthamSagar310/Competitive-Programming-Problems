for _ in range(int(input())):
    n, m, x = map(int, input().split())

    # original
    r, c = (x-1) % n, (x-1) // n

    # transformed 
    print(r * m + c + 1)
