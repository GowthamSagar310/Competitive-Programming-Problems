from collections import Counter
n, m = map(int, input().split())
arr = list(map(int, input().split()))
freq = Counter(arr)
if len(freq) == n:
    print(min(freq.values()))
else:
    print(0)
