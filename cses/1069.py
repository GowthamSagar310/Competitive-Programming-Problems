s = input()
maxi = c = 1
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        c += 1
        maxi = max(maxi, c)
    else:
        c = 1
print(maxi)