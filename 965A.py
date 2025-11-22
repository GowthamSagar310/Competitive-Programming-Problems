k, n, s, p = map(int, input().split())

# 1 sheet -> s planes
# n/s sheet -> n planes
# total planes = n * k 
# total sheets = k * (n / s)

ans = (n-1) // s + 1
ans = k * ans
ans = (ans - 1) // p + 1 
print(ans)
