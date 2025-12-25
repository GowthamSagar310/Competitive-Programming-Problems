from collections import Counter 

s = input()
t = input()

# no extra letters and no less letters

all = Counter(input())
for l in s: all[l] -= 1
for l in t: all[l] -= 1

print("NO" if any(v != 0 for v in all.values()) else "YES")