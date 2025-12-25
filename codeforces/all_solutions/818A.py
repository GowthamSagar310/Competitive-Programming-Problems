n, k = map(int, input().split())
d = n // (2 * (k+1))
c = k * d 
print(d, c, n-(c+d)) 