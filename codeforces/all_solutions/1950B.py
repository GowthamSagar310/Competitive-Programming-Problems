for _ in range(int(input())):
    n = int(input())

    row_start_dot = True
    matrix = [["" for _ in range(2 * n)] for _ in range(2 * n)]

    for r in range(2 * n):
        if r % 2 == 0: 
            row_start_dot = not row_start_dot
        current = "." if row_start_dot else "#"
        for c in range(2 * n):
            if c > 0 and c % 2 == 0:
                if current == "#": current = "."
                else: current = "#"
            matrix[r][c] = current
    
    for row in matrix:
        print("".join(row))