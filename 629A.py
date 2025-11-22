n = int(input())
cols = [0] * n
pairs = 0
for _ in range(n):
    s = input()
    rc = 0 
    for i, l in enumerate(s):
        if l == "C":
            rc += 1
            cols[i] += 1
    pairs += ((rc) * (rc-1)) // 2

for val in cols:
    pairs += ((val) * (val-1)) // 2

print(pairs)