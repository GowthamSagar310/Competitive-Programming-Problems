def get_pocket(dx, dy, s):
    if   dx == 1 and dy == 1: return [s, s]
    elif dx == -1 and dy == -1: return [0, 0]
    elif dx == -1 and dy == 1: return [s, 0]
    else: return [0, s]

for _ in range(int(input())):
    n, s = map(int, input().split())
    count = 0
    for _ in range(n):
        dx, dy, x1, y1 = map(int, input().split())
        x2, y2 = get_pocket(dx, dy, s)
        slope = (y2-y1) / (x2-x1)
        if abs(slope) == 1:
            count += 1
    print(count)