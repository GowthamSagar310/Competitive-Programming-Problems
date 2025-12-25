# def print_matrix(matrix):
#     for row in matrix:
#         print(" ".join(map(str, row)))


# for _ in range(int(input())):
#     n, m = map(int, input().split())
#     matrix = []
#     for i in range(n):
#         row = list(map(int, input().split()))
#         matrix.append(row)

#     if n == 1 and m == 1:
#         print(-1)
#         continue
#     elif m == 1:
#         first_val = matrix[0][0]
#         for i in range(n-1):
#             matrix[i][0] = matrix[i+1][0]
#         matrix[n-1][0] = first_val
#     else:
#         for row in range(n):
#             first_val = matrix[row][0]
#             for i in range(m-1):
#                 matrix[row][i] = matrix[row][i+1]
#             matrix[row][m-1] = first_val
    
#     print_matrix(matrix)


# another simple approach to write this is to shift numbers diagonally
# for _ in range(int(input())):
#     n, m = map(int, input().split())
#     matrix = []
#     for i in range(n):
#         row = list(map(int, input().split()))
#         matrix.append(row)
    
#     if n == 1 and m == 1:
#         print(-1)
#         continue
#     elif n == 1:
#         # if there is only row, cyclically shift through columns
#         for c in range(m):
#             print(matrix[0][(c+1) % m], end=" ")
#         print()
#     else:
#         # cyclically shift through rows
#         # print(second row, third row, ... , first row)
#         for r in range(n):
#             for c in range(m):
#                 print(matrix[(r+1) % n][c], end=" ")
#             print()

# we can simplify this a lot by combining above two conditions
for _ in range(int(input())):
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    if n == 1 and m == 1:
        print(-1)
        continue
    else:
        # cyclically shift through rows and columns
        for r in range(n):
            for c in range(m):
                print(matrix[(r+1) % n][(c+1)%m], end=" ")
            print()
