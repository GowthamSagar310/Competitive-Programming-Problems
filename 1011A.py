n, k = map(int, input().split())
s = input()
ans = 0
found = False
s = sorted(s)
prev = -2
count = 0
for i in range(n):
    if ord(s[i])-prev >= 2:
        prev = ord(s[i])
        ans += ord(s[i])-ord('a')+1
        count += 1
        if count >= k:
            found = True
            break
if not found:
    print(-1)
else:
    print(ans)
