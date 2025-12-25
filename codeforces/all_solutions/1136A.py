n = int(input())
pages = []
for _ in range(n):
    l, r = map(int, input().split())
    pages.append((l, r))
k = int(input())
i = 0
while i < n:
    l, r = pages[i]
    if l <= k <= r:
        break
    i += 1
print(n-i)