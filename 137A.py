s = input()
n = len(s)
count = 0
l = 0
for r in range(n):
    if s[l] == s[r]:
        if r-l+1 == 5:
            l = r+1
            count += 1
    else:
        l = r
        count += 1
print(count if l == n else count+1)