for _ in range(int(input())):
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    
    # for each diagonal, we need to find the max abs value
    # and add them

    # i = n-1 j = 0
    # i = n-2 j = 1
    # i = n-3 j = 2

    total = 0
    for i in range(n-1, -1, -1):
        maxi = float("-inf")
        iters = 0
        while iters < n-i:
            diagonal_value = matrix[i+iters][iters]
            if diagonal_value < 0:
                maxi = max(maxi, -diagonal_value)
            iters += 1
        if maxi != float("-inf"):
            total += maxi

    # incomplete