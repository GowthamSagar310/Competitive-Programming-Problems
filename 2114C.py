for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    """
    1 2 3 4 5 6
    1 3 5 = 3
    
    1 2 3
    1 3 = 2

    1 2 2 4
    """
    remove = 0
    i = 0
    while i < n-1:
        j = i+1
        while j < n and arr[j]-arr[i] <= 1:
            j += 1
        remove += j-i-1
        i = j
    print(n-remove)