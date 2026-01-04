n1, n2, n3, n4 = map(int, input().split())
x, y, z, abc = sorted([n1, n2, n3, n4])

"""

they are giving in random order


a+b = x
b+c = y
c+a = z

a+b+c > a+b, b+c, c+a

finding "a"
= a+b - (b+c) + c+a
= a+b-b-c+c+a
= 2a = x-y+z
a = (x-y+z) // 2
b = (y-z+x) // 2
c = (z-x+y) // 2
"""

a = (x-y+z) // 2
b = (y-z+x) // 2
c = (z-x+y) // 2
print(*[a, b, c])