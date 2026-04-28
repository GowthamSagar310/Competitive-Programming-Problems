a = int(input())
b = int(input())
c = int(input())

"""

when is a + b > a * b ? 
one or more of them are 1s

and also a + b + c > a * b * c ? 
two or more of them are 1s

"""
print(max(a + b + c, (a + b) * c, a * (b + c), a * b * c))