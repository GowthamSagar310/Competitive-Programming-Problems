from collections import Counter
n, k = map(int, input().split())
s = input()
c = Counter(s)
if max(c.values()) > k:
    print("NO")
else:
    print("YES")