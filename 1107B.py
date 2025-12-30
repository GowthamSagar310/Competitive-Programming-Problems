# digit root = (sum of digits) % 9 = num % 9
for _ in range(int(input())):
    k, dr = map(int, input().split())
    
    # first number is always dr
    # second number = dr + 9 
    # since adding 9 does not change num % 9 -> digit root is not changed

    print(dr + (k-1) * 9)