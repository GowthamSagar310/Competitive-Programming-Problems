n = int(input())
s = input()
substrings = 0
for i,l in enumerate(s):
    if int(l) % 2 == 0:
        substrings += i+1
print(substrings)