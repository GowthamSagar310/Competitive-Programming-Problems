n, t = map(int, input().split())
s = list(input())

def solve(s, n, t):
    for _ in range(t):
        found = False
        i = 0
        while i < n-1:
            if s[i] == "B" and s[i+1] == "G":
                found = True
                s[i], s[i+1] = s[i+1], s[i]
                i += 1
            i += 1
        if not found: break
    return "".join(s)

print(solve(s, n, t))