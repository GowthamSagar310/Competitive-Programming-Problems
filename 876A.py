n = int(input())
a = int(input())
b = int(input())
c = int(input())
if n == 1:
    print(0)
else:
    if min(a, b, c) == a or min(a, b, c) == b:
        print(min(a, b) * (n-1))
    else:
        print(min(a, b) + c * (n-2))
