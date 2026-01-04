for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    # this is not as simple as adding +1 when not divisible
    # because there can be 1 as ai
    # ai+1 / ai will always be divisible no matter how many +1s are added

    for i in range(n):
        if arr[i] == 1:
            arr[i] += 1
    
    for i in range(1, n):
        if arr[i] % arr[i-1] == 0:
            arr[i] += 1
    
    print(*arr)