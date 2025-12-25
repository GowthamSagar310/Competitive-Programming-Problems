for _ in range(int(input())):
    
    matrix = []
    for _ in range(8):
        matrix.append(input())

    res = []
    for row in matrix:
        for char in row:
            if char != ".":
                res.append(char)
    
    print("".join(res))