for _ in range(int(input())):
    n, a, b = map(int, input().split())
    maxi = a
    for i in range(n):
        maxi = max(maxi, (a + b * (i+1)) % n)
    print(maxi)