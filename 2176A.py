for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    l = 0
    count = 0
    for r in range(n):
        if arr[l] > arr[r]:
            count += 1
        else:
            l = r
    print(count)