for _ in range(int(input())):
    n = int(input())

    """
    1. all numbers should be unique.
    1+2+3... 9 = 45
    maximum number possible with unique digits = 45
    so, 46 to 50 are never possible

    2. 1 to 9 are anyway possible

    3. is there a way to use num % 9 = (sum of digits) % 9 
    """

    if n < 10: print(n); continue
    if n > 45: print(-1); continue
    res = 0
    i = 0
    for val in [9,8,7,6,5,4,3,2,1]:
        res = val * (10 ** i) + res
        n -= val
        if n < 10 and n < val:
            i += 1
            res = n * (10 ** i) + res
            n = 0
            break
        i += 1
    print(res)