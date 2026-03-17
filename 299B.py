n, k = map(int, input().split())
s = input()

def solve(s, n, k):
    if s[0] == "#" or s[n-1] == "#": return False
    i = 0
    while i < n:
        flag = False
        for j in range(min(i+k, n-1), i, -1):
            if j == n-1: return True
            if s[j] == ".":
                flag = True
                i = j
                break
        if not flag: return False
    return True

print("YES" if solve(s, n, k) else "NO")