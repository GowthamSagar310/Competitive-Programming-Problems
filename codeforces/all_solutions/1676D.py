# def get_top_left_score(r, c):
#     score = 0
#     while r >= 0 and c >= 0:
#         score += grid[r][c]
#         r -= 1
#         c -= 1
#     return score

# def get_top_right_score(r, c):
#     score = 0
#     while r >= 0 and c < m:
#         score += grid[r][c]
#         r -= 1
#         c += 1
#     return score

# def get_bottom_left_score(r, c):
#     score = 0
#     while r < n and c >= 0:
#         score += grid[r][c]
#         r += 1
#         c -= 1
#     return score

# def get_bottom_right_score(r, c):
#     score = 0
#     while r < n and c < m:
#         score += grid[r][c]
#         r += 1
#         c += 1
#     return score

# for _ in range(int(input())):
#     n, m = map(int, input().split())
#     grid = []
#     for _ in range(n):
#         grid.append(list(map(int, input().split())))
#     maxi = 0
#     for r in range(n):
#         for c in range(m):
#             tl = get_top_left_score(r-1, c-1)
#             tr = get_top_right_score(r-1, c+1)
#             bl = get_bottom_left_score(r+1, c-1)
#             br = get_bottom_right_score(r+1, c+1)
#             maxi = max(maxi, tl + tr + bl + br + grid[r][c])
#     print(maxi)

