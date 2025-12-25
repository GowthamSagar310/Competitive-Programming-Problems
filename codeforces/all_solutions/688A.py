n, d = map(int, input().split())
res = 0
c = 0
for i in range(d):
    s = input()
    if s.count("1") == n:
        c = 0
    else:
        c += 1
    res = max(res, c)
print(res)