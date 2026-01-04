def solve(arr, n):
    arr.sort()
    for i in range(1, n):
        if arr[i]-arr[i-1] > 1:
            return False
    return True

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print("YES" if solve(arr, n) else "NO") 