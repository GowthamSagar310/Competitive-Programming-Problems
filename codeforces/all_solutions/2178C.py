def solve(i_val, arr):
    n1, n2 = 1, 2
    while n1 < n and n2 < n:
        if i_val + arr[n1] >= i_val - arr[n2]:
            # choosing the first value
            i_val += arr[n1]
            n1 = n2 
            n2 = n2+1
        else:
            i_val -= arr[n2]
            n2 = n2+1
    return i_val        

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    v1 = solve(arr[0], arr)
    arr[0], arr[1] = arr[1], arr[0]
    v2 = solve(-arr[0], arr)
    print(max(v1, v2))