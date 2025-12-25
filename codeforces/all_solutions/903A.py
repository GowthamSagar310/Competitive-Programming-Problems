def solve(n):
    b = 0
    while 7 * b <= n:
        left = n - 7 * b
        if left % 3 == 0:
            return "YES"
        b += 1
    return "NO"

for _ in range(int(input())):
    n = int(input())
    print(solve(n))