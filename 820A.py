c, v0, v1, a, l = map(int, input().split())

"""
v0
v0 + 1a - 1l 
v0 + 2a - 1l
v0 + n * v0 + (n*(n+1))//2 * a - n * l >= c
"""

days = 0
i = 0
while c > 0:
    pages = min(v1, v0 + i * a)
    pages -= l if i > 0 else 0
    c -= pages
    days += 1
    i += 1
print(days)

