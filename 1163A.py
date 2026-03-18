n, m = map(int, input().split())

"""
maximize the number of groups. 
"""

if n == m: print(0)
elif m == 0 or m == 1: print(1)
else:
    
    if m <= (n // 2):
        print(m)
    else:
        print(n-m)

