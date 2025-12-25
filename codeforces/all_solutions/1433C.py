def solve(arr):
    maxi = max(arr)
    for i, val in enumerate(arr):
        if val == maxi:
            if i+1 < n and val > arr[i+1]:
                return i+1 # one based indexing 
            if i-1 >= 0 and val > arr[i-1]:
                return i+1 # one based indexing 
    return -1

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    # find the maximum value which is next to something less
    print(solve(arr))
