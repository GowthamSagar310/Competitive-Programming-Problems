from collections import Counter
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    c = Counter(arr)        
    arr_s = sorted([v for v in c.values()])
    maxi = 0
    for i in range(len(c)):
        maxi = max(maxi, arr_s[i] * (len(c)-i))
    print(maxi)
    
