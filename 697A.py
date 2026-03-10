t, s, x = map(int, input().split())
"""
t

t + s 
t + s + 1

t + 2s
t + 2s + 1


t + k * s = x
is k integer ? 

"""

k1 = ((x - t) % s) == 0
k2 =  (x - t - 1) != 0 and ((x - t - 1) % s) == 0

if k1 or k2:
    print("YES")
else:
    print("NO")

