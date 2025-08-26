from collections import Counter

def solve(s, k):
    counter = Counter(s)
    odd_count = sum([1 if v & 1 else 0 for v in counter.values()])
    return "YES" if odd_count-1 <= k else "NO"

for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    print(solve(s, k))
