def solve(s):
    x, y = 0, 0
    for l in s:
        if l == "L": x -= 1
        if l == "R": x += 1
        if l == "U": y += 1
        if l == "D": y -= 1
        if x == 1 and y == 1:
            return "YES"
    return "NO"

for _ in range(int(input())):
    n = int(input())
    s = input()
    print(solve(s))

