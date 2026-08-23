for _ in range(int(input())):
    n = int(input())
    r = n % 12
    if r == 10:
        if n >= 22:
            print(*[22, n-22])
        else:
            print(-1)
    else:
        print(*[r, n-r])