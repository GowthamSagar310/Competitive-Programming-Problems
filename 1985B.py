for _ in range(int(input())):
    n = int(input())    
    maxi = float("-inf")
    ans = -1
    for x in range(2, n+1):
        k = (n // x)
        total = x * (k * (k + 1)) // 2
        if total > maxi:
            maxi = total
            ans = x
    print(ans)
