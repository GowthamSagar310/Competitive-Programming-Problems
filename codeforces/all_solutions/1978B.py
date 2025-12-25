for _ in range(int(input())):
    n, a, b = map(int, input().split())

    # original profit = n * a
    # 
    # k buns 
    # (b-1+1) + (b-2+1) + (b-3+1) + (b-k+1)
    # k * b - (1 + 2 + .. k) + k
    # k * b + k - ((k * (k+1)) // 2)
    #
    # n-k buns
    # (n-k) * a
    # 
    # f(p) = k * b + k - (1 + 2 + .. k) + (n-k) * a
    # 
    # k * b + k - (1 + 2 + .. k) + (n-k) * a > n * a
    # 2 * k * (b-a) + 2 * k > k^2 + k
    # 2 * k * (b-a) > k^2-k
    # 2 * (b-a) > k-1
    # 2 * (b-a) + 1 > k
    # k < 2b - 2a + 1
    
    # b + 1 - (1/2) * (2k+1) -a = 0
    # b-a+1 = (2k+1) / 2
    # 2(b-a+1)-1 = 2k
    # (b-a+1)-(1/2) = k
    # b-a-1/2 = k
    
    k = min(n, max(0, b-a))
    print(k * b + k - ((k * (k+1)) // 2) + (n-k) * a)