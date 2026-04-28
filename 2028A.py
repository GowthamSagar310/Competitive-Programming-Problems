def solve(s, n, a, b):

    dx, dy = 0, 0
    for char in s:
        if char == 'N': dy += 1
        elif char == 'S': dy -= 1
        elif char == 'E': dx += 1
        elif char == 'W': dx -= 1

    cx, cy = 0, 0
    found = False
    check_points = [(0, 0)]
    for char in s:
        if char == 'N': cy += 1
        elif char == 'S': cy -= 1
        elif char == 'E': cx += 1
        elif char == 'W': cx -= 1
        check_points.append((cx, cy))
    
    for xi, yi in check_points:
        rem_x = a - xi
        rem_y = b - yi
        if dx == 0 and dy == 0:
            if rem_x == 0 and rem_y == 0:
                found = True
                break

        elif dx == 0 and dy != 0:
            if rem_x == 0 and rem_y % dy == 0 and rem_y // dy >= 0:
                found = True
                break

        elif dx != 0 and dy == 0:
            if rem_y == 0 and rem_x % dx == 0 and rem_x // dx >= 0:
                found = True
                break

        elif dx != 0 and dy != 0:
            if rem_x % dx == 0 and rem_y % dy == 0:
                kx = rem_x // dx
                ky = rem_y // dy
                if kx == ky and kx >= 0:
                    found = True
                    break
    
    return found


for _ in range(int(input())):
    n, a, b = map(int, input().split())
    s = input()
    print("YES" if solve(s, n, a, b) else "NO")
