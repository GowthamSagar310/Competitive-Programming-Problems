n = int(input())
x = y = z = 0
for _ in range(n):
    fx, fy, fz = map(int, input().split())
    x += fx
    y += fy 
    z += fz 
print("YES" if x == 0 and y == 0 and z == 0 else "NO")