n, k = map(int, input().split())
s = input()

freq = [0] * k
for l in s: freq[ord(l.lower()) - ord('a')] += 1
min_freq = min(freq)

print(k * min_freq)

