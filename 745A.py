s = input()
n = len(s)
words = set()
for k in range(n):
    words.add(s[-k:] + s[:-k])
print(len(words))