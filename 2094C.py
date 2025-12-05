for _ in range(int(input())):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    res = [0] * (2 * n)
    for i in range(n):
        for j in range(n):
            res[i+1+j+1-1] = matrix[i][j]

    total = (2*n * (2*n+1)) // 2
    res[0] = total - sum(res)
    print(*res)
    
    # (1,1) (1,2) (1,3) 2 3 4
    # (2,1) (2,2) (2,3) 3 4 5
    # (3,1) (3,2) (3,3) 4 5 6
    # [2, 2n] sum is present, except 1
    # so the first element is missing
