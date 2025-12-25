s = input()
p = "heidi"
i = j = 0
while i < len(s) and j < 5:
    if s[i] == p[j]:
        j += 1
    i += 1
print("YES" if j == 5 else "NO")