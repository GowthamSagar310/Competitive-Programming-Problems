n, k = map(int, input().split())
evens = n // 2
odds = (n+1) // 2

if k <= odds: 
    print((2 * k)-1)
else:
    k -= odds
    print(2*k)
