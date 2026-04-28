def solve(s, l, r):
    # first letter
    for i in range(l-1, -1, -1):
        if s[l] == s[i]:
            return True
    
    # last letter
    for i in range(r+1, n):
        if s[r] == s[i]:
            return True
    
    return False

for _ in range(int(input())):
    n, q = map(int, input().split())
    s = input()
    for _ in range(q):
        l, r = map(int, input().split())
        print("YES" if r-l+1 >= 2 and solve(s, l-1, r-1) else "NO")