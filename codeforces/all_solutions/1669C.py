def solve(arr):
    for i in range(n):
        if i > 1:
            if arr[i] & 1 != arr[i-2] & 1:
                return "NO"
    return "YES"

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr))    
    
    