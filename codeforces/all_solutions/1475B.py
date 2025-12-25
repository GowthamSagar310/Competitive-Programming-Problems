for _ in range(int(input())):
    n = int(input())

    q = n // 2020
    r = n % 2020

    if q < 1 or r > q:
        print("NO")
    else:
        print("YES")