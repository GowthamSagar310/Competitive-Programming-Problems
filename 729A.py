n = int(input())
s = input()
res = []
i = 0
while i < n:
    if s[i:i+3] == "ogo":
        j = i+3
        while j < n:
            if s[j:j+2] == "go":
                j+=2
            else:
                break
        res.append("*"*3)
        i = j
    else:
        res.append(s[i])
        i += 1
print("".join(res))