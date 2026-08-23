for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    s = sum(arr[i] for i in range(2*n-2, -1, -2))
    print(s)
