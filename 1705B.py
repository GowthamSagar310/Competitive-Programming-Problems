for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    # every zero takes one step to fill 

    i = 0
    while i < n and arr[i] == 0:
        i += 1
    if i >= n-1:
        print(0)
    else:
        print(sum(arr[i] if arr[i] != 0 else 1 for i in range(i, n-1)))