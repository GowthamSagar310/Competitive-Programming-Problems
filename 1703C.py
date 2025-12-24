for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        m, s = input().split()
        m = int(m)
        for l in s:
            if l == 'D':
                arr[i] = (arr[i] + 1) % 10
            else:
                arr[i] = (arr[i] - 1) % 10
    print(*arr)