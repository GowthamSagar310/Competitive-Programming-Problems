n = int(input())
s = input()

x_count = s[:3].count("x")
ops = 1 if x_count == 3 else 0
l = 0 
for r in range(3, n):
    x_count += s[r] == "x"
    x_count -= s[l] == "x"
    l += 1
    if x_count == 3:
        ops += 1
print(ops)