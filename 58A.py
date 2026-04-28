s = input()
t = "hello"

j = 0
for i, l in enumerate(s):
    if j < len(t) and s[i] == t[j]:
        j += 1

print("YES" if j == 5 else "NO")