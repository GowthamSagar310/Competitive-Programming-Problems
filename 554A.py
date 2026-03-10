s = input()
ss = set()

for i in range(26):
    letter = chr(i + ord('a'))
    for j in range(len(s)+1):
        ss.add(s[:j] + letter + s[j:])

print(len(ss))