import math

for _ in range(int(input())):
    n, k = map(int, input().split())

    # remove k^x from n 
    # k ^ x = n
    # x = 0 to n
    
    # log base k = x
    # int(x) -> minimize n-k^x

    if k == 1:
        print(n)
    else:
        ops = 0
        while n > 0:
            ops += n % k
            n //= k
        print(ops)