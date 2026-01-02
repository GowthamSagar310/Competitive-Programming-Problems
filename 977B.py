from collections import defaultdict
n = int(input())
s = input()
m = defaultdict(int)
maxi = 0
for i in range(1, n):
    m[s[i-1] + s[i]] += 1
    if m[s[i-1] + s[i]] > maxi:
        maxi = m[s[i-1] + s[i]]
        ans = s[i-1] + s[i]
print(ans)
