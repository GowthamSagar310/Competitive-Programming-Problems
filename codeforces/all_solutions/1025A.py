n = int(input())
s = input()
freq = [0] * 26
found = False
if len(s) == 1: 
    found = True
else:
    for l in s:
        index = ord('a')-ord(l)
        freq[index] += 1
        if freq[index] > 1:
            found = True
            break
print("Yes" if found else "No")