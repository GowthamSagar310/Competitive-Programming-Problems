from collections import Counter
def solve(arr, n):
    arr.sort()
    if arr[0] != 0:
        return False
    else:
        if arr[1] != 0:
            return True
        else:
            return 1 in arr[2:]
    
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print("YES" if solve(arr, n) else "NO")    
