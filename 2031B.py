def solve(arr):
    for i, val in enumerate(arr):
        if abs(val-1-i) >= 2:
            return False
    return True

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print("YES" if solve(arr) else "NO")
