def solve(arr, m):
    # check if sorted
    for i in range(1, m):
        if arr[i] <= arr[i-1]:
            # not sorted
            return 1
    
    # sorted
    return n-arr[-1]+1

        
for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(arr, m))    

