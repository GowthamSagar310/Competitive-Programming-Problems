for _ in range(int(input())):
    n, s, t = map(int, input().split())
    print((n-min(s,t))+1)