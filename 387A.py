h1, m1 = map(int, input().split(":"))
h2, m2 = map(int, input().split(":"))

"""
current time: h1: m1
total duration: h2: m2
"""

if h1 >= h2:
    h = h1-h2
else:
    h = 24 + h1 - h2

if m1 >= m2:
    m = m1-m2
else:
    h -= 1
    if h < 0: h += 24
    m = 60 + m1 - m2

print(f"{h:02d}:{m:02d}")