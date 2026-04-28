s = input()
res = []
vowels = set("aeiouyAEIOUY")
for l in s:
    if l not in vowels:
        res.append(".")
        res.append(l.lower())
print("".join(res))
