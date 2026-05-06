for _ in range(int(input())):
    n = int(input())
    s = input()
    prefix = [0] * n
    suffix = [0] * n

    seen = set()
    for i in range(n):
        seen.add(s[i])
        prefix[i] = len(seen)
    
    seen.clear()
    for i in range(n-1, -1, -1):
        seen.add(s[i])
        suffix[i] = len(seen)
        
    maxi = 2
    for i in range(n-1):
        maxi = max(maxi, prefix[i] + suffix[i+1])
    print(maxi)