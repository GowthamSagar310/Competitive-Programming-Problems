n = int(input())
b = 0
while n:
    if n % 2 != 0:
        n -= 1
        b += 1
    else:
        n //= 2
print(b)