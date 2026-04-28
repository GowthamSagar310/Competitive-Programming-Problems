for _ in range(int(input())):
    n = int(input())
    s = n * (n-1)

    MOD = (10**9)+7
    r = 1
    for i in range(1, n+1):
        r *= i
        r %= MOD
    
    r %= MOD
    s %= MOD
    r = (r * s) % MOD
    print(r)

