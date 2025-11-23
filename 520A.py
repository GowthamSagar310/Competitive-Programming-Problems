n = int(input())
s = input()

if n < 26:
    print("NO")
else:
    present = [False] * 26
    for l in s:
        present[ord(l.lower())-ord('a')] = True
    print("YES" if sum(present) == 26 else "NO")