for _ in range(int(input())):
    n, m = map(int, input().split())
    if n < m:
        print("NO")
    elif (n-m) & 1:
        print("NO")
    else:
        print("YES")