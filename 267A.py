def solve(a, b):
    total_ops = 0
    while a > 0 and b > 0:
        if a > b: a, b = b, a
        diff = b-a
        ops = (diff // a) + 1
        total_ops += ops
        b -= a * ops
    return total_ops

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(solve(a, b))
