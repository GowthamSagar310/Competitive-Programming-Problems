for _ in range(int(input())):
    w, h, n = map(int, input().split())

    sheets = 1
    while h != 1 and h % 2 == 0:
        sheets *= 2
        h //= 2

    while w != 1 and w % 2 == 0:
        sheets *= 2
        w //= 2
    
    print("YES" if sheets >= n else "NO")

