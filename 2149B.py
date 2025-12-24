for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    diff = float("-inf")
    for i in range(1, n, 2):
        diff = max(diff, abs(arr[i]-arr[i-1]))
    print(diff)