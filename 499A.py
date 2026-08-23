n, x = map(int, input().split())
ct = 1
sw = 0
for _ in range(n):
    l, r = map(int, input().split())
    k = (l-ct) // x
    sw += l-(ct + k * x)
    sw += (r-l+1)
    ct = r+1
print(sw)
