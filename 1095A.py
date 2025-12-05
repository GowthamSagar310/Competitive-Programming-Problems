n = int(input())
s = input()
res = []
i = 0
j = 2
while i < n:
    res.append(s[i])
    i += j
    j += 1
print("".join(res))  