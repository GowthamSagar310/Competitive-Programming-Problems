for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    possible = -1
    for i in range(n):
        if i % 2 == 0:
            possible = max(possible, arr[i])
    print(possible)
