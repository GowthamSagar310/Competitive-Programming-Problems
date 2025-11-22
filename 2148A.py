for _ in range(int(input())):
    x, n = map(int, input().split())
    print(x if n & 1 else 0)