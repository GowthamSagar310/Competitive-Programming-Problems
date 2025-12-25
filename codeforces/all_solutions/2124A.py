def solve(arr, n):
    i = 1
    while i < n:
        if arr[i] < arr[i-1]:
            return True
        i += 1
    return False

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    if solve(arr, n):
        print("YES")
        print(n)
        print(*arr)
    else:
        print("NO")