# min top left, min bottom left
# max top right, max bottom right

r, c = map(int, input().split())
min_left = min_top = float("inf")
max_right = max_bottom = float("-inf")
matrix = []
for i in range(r):
    row = input()
    matrix.append(row)
    for j, col in enumerate(row):
        if col == "*":
            min_left = min(min_left, j)
            max_right = max(max_right, j)
            min_top = min(min_top, i)
            max_bottom = max(max_bottom, i)

for i in range(min_top, max_bottom+1):
    for j in range(min_left, max_right+1):
        print(matrix[i][j], end='')
    print()
            
