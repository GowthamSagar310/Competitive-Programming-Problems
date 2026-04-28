from math import ceil
n, m = map(int, input().split())

# O(N)
# def solve(n, m):
#     max_moves = n
#     min_moves = (n // 2) + n % 2
#     for moves in range(min_moves, max_moves+1):
#         if moves % m == 0:
#             return moves
#     return -1
# print(solve(n, m))

#     max_moves = n
#     min_moves = (n // 2) + n % 2
# what is the number >= min_moves which is multiple of m ? 
# ceil(min_moves / m) * m

max_moves = n
min_moves = (n // 2) + n % 2
ans = ceil(min_moves / m) * m
if ans > max_moves:
    print(-1)
else:
    print(ans)