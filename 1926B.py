def solve(matrix):
    prev_one_count = -1
    for row in matrix:
        one_count = row.count("1")
        if one_count:
            if prev_one_count == -1:
                prev_one_count = one_count
            elif prev_one_count != one_count:
                return "TRIANGLE"
    return "SQUARE"

for _ in range(int(input())):
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(input())
    print(solve(matrix))
