def solve(arr):
    c = 0
    negative_present = False
    for val in arr:
        if val == -1:
            negative_present = True
            c += 1
            if c > 1:
                return sum(arr)+4                
        else:
            c = 0
    if negative_present:
        return sum(arr)
    else:
        return sum(arr)-4

def solve2(arr):
    s = sum(arr)
    ans = float("-inf")
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            if arr[i] == 1:
                ans = max(ans, s-4)
            else:
                ans = max(ans, s+4)
        else:
            ans = max(ans, s)
    return ans

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve2(arr))
