n = int(input())
schedule = []
horizontal, vertical = set(), set()
for _ in range(n * n):
    h, v = map(int, input().split())
    schedule.append((h, v))
    
ans = []
for i, (h, v) in enumerate(schedule):
    if h not in horizontal and v not in vertical:
        ans.append(i+1)
        horizontal.add(h)
        vertical.add(v)
print(*ans)
