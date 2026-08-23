n, m = map(int, input().split())
"""
3 4
1 1
1 2
1 3
1 4
2 1
3 1
"""

print(n+m-1)
for j in range(1, m+1):
    print(1, j)
for i in range(2, n+1):
    print(i, 1)

