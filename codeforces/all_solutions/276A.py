n, k = map(int, input().split())
maxi = float("-inf")
for _ in range(n):
    f, t = map(int, input().split())
    if t > k:
        joy = f - (t-k)
    else:
        joy = f
    maxi = max(maxi, joy)
print(maxi)