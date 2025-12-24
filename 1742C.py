def solve(grid):
    for r in range(8):
        row = grid[r]
        r_count = row.count("R")
        if r_count == 8:
            return "R"
    return "B"

for _ in range(int(input())):
    input()
    grid = []
    for _ in range(8):
        grid.append(input())
    print(solve(grid))