def solve(s, n):
    for i in range(1, n, 3):
        if (i+1 >= n) or s[i] != s[i+1]:
            return False
    return True
    
for _ in range(int(input())):
    n = int(input())
    s = input()
    print("YES" if solve(s, n) else "NO")
