def solve(n, arr):
    ops = 0 
    for i in range(n-2, -1, -1):
        if arr[i+1] == 0:
            return -1
        while arr[i] >= arr[i+1]:
            arr[i] //= 2
            ops += 1
    return ops

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(n, arr))
