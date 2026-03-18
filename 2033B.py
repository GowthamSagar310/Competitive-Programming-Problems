for _ in range(int(input())):
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    
    ops = 0
    for i in range(n):
        for j in range(n):
            val = matrix[i][j]
            if val < 0:
                ops += abs(val)
                r, c = i, j
                while r < n and c < n:
                    if matrix[r][c] < 0:
                        matrix[r][c] += abs(val)
                        matrix[r][c] = min(0, matrix[r][c])
                    r += 1
                    c += 1
    print(ops)