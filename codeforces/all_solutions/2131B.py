for _ in range(int(input())):
    n = int(input())

    res = [-1] * n
    for i in range(1, n, 2):
        if i + 1 < n:
            res[i] = 3
        else:
            res[i] = 2
    
    print(*res)