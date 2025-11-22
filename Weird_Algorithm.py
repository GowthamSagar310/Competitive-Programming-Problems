n = int(input())
print(n, end=" ")
while n != 1:
    if n & 1:
        n = 3 * n + 1
        print(n, end = " ")
    else:
        n = n // 2
        print(n, end = " ")
