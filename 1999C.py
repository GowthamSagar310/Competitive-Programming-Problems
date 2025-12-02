def solve(s, m, intervals):
    prev = 0
    for start, end in intervals:
        if start - prev >= s:
            return "YES"
        prev = end
    return "YES" if m-prev >= s else "NO"

for _ in range(int(input())):
    n, s, m = map(int, input().split())
    intervals = []
    for _ in range(n):
        start, end = map(int, input().split())
        intervals.append((start, end))
    print(solve(s, m, intervals))