l = int(input())
p = int(input())
q = int(input())

"""

say they meet at x distance from left, l-x from right

speed / distance = speed / distance

p / x = q / l-x

pl - px = qx
pl = x (p + q)
x = pl / (p + q)

"""

print(p * l / (p + q))