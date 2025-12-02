for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    if k == 1:
        # if k == 1, 
        # I can make single elements bigger
        print(n-2 // 2 + ((n-2) & 1))
    else:
        # if k > 1
        # elements increase by 1 combinedly
        # so if previously it is not peak, 
        # it wont be after operations
        count = 0
        for i in range(1, n-1):
            if arr[i] > arr[i-1] + arr[i+1]:
                count += 1
        print(count)