from collections import Counter
for _ in range(int(input())):
    n, c, d = map(int, input().split())
    b = list(map(int, input().split()))
    a = min(b)
    freq = Counter(b)
    grid = [[0 for _ in range(n)] for _ in range(n)]
    grid[0][0] = a
    possible = True
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0: continue
            top, left = -1, -1
            if i > 0 and j > 0:
                top = grid[i-1][j]
                left = grid[i][j-1]
                x1 = top + c
                x2 = left + d
                if x1 == x2 and freq[x1] > 0:
                    freq[x1] -= 1
                    grid[i][j] = x1
                else:
                    possible = False
            elif i > 0 and freq[grid[i-1][j] + c] > 0:
                freq[grid[i-1][j]] -= 1
                grid[i][j] = grid[i-1][j] + c
            elif j > 0 and freq[grid[i][j-1] + d] > 0:
                freq[grid[i][j-1]+d] -= 1
                grid[i][j] = grid[i][j-1]+d
            else:
                possible = False
        if not possible: break
    print("YES" if possible else "NO")


