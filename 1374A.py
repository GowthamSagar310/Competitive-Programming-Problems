for _ in range(int(input())):
    x, y, n = map(int, input().split())
    
    # find k 0 <= k <= n
    # such that k mod x = y
    # k = q * x + y
    # 0 <= k <= n 
    # 0 <= q * x + y <= n
    # -y <= q * x <= n-y
    # -y / x <= q <= (n-y) / x

    # print(x * ((n - y) // x) + y)

    # another way to solve this problem
    # think of it in a different way 

    # what is the current remainder ? n % x
    # if we remove that from n, n = n - n % x
    # then the remainder would be 0 
    # then to make the remainder y, we can simply add y
    # so k = n - n % x + y
    # 
    # but what this k > n ? 
    # n - n % x -> remainder 0 
    # n - n % x - x -> still remainder 0
    # now we can add y 

    k = n - (n % x) + y
    if k <= n:
        print(k)
    else:
        print(k-x)

    # observe the constraints 