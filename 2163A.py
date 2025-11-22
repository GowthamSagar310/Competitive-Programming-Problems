def solve(arr, n):
    arr.sort()
    for i in range(1, n-1, 2):
        if arr[i] != arr[i+1]:
            return "NO"
    return "YES"

for _ in range(int(input())):
    
    n = int(input())
    arr = list(map(int, input().split()))

    # guaranteed winning strategy means
    # no matter what kalamaki does, souvlaki should be able to win. 

    # so, we should be able to keep same values on 
    # (2, 3), (4, 5), (6, 7) etc.
    # so even if kalamaki swaps, there is no harm

    print(solve(arr, n))