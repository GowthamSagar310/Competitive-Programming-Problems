s, n = map(int, input().split())
dragons = []
for _ in range(n):
    x, y = map(int, input().split())
    dragons.append((x, y))

def solve(s, dragons):
    dragons.sort()
    for x, y in dragons:
        if s <= x:
            return False
        s += y
    return True

print("YES" if solve(s, dragons) else "NO")