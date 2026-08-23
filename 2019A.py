for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 1:
        print(arr[0]+1)
    else:
        a = [arr[i] for i in range(0, n, 2)]
        b = [arr[i] for i in range(1, n, 2)]
        print(max(max(a)+len(a), max(b)+len(b)))
    