for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    # combos
    # 1. fix first, take max to the end
    # 2. fix end, take min to the first
    # 3. if arr[i] > arr[i+1], we can make these first and last by rotating

    maxi = max(max(arr)-arr[0], arr[-1]-min(arr))
    for i in range(n):
        if arr[i] >= arr[(i+1) % n]:
            maxi = max(maxi, arr[i]-arr[(i+1) % n])
    print(maxi)
