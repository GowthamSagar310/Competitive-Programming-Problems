n, t = map(int, input().split())

# q = 10 ** (n-1)
# r = q % t
# num = q + (t-r if r else 0)
# print(-1 if len(str(num)) != n else num)


if t == 10:
    if n == 1:
        print(-1)
    else:
        print(10 ** (n-1))
else:
    print(f"{t}"*n)