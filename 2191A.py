def solve(arr, n):
    for i in range(1, n):
        if abs(arr[i]-arr[i-1]) % 2 == 0:
            return False
    return True

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print("YES" if solve(arr, n) else "NO")