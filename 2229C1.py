for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = []
    ops = 0
    for i in range(n-1, -1, -1):
        if ops % 2: arr[i] *= -1
        if arr[i] > 0:
            ans.append(i+1)
            ops += 1
    print(ops)
    print(*ans)
