x = input()
y = input()

"""
f(x, z) = y
min(x[i], z[i]) = y

if x[i] > y:
    # z[i] should be less x[i]+1
if x[i] <= y:
    z[i] = x[i]
"""

def solve(x, y):
    z = ""
    for i in range(len(x)):
        if x[i] > y[i]:
            z += y[i]
        elif x[i] < y[i]:
            return -1
        else:
            z += x[i]
    return z

print(solve(x, y))