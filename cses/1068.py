n = int(input())
if n == 1:
    print(1)
else:
    res = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n+1
        res.append(n)
    print(*res)