a, b, c, d = map(int, input().split())

"""
max(3 * a / 10, a - (a / 250) * c)
"""

def score(p, t):
    return max(3 * p / 10, p - (p * t) / 250)

m = score(a, c)
v = score(b, d)
if m > v:
    print("Misha")
elif v > m:
    print("Vasya")
else:
    print("Tie")