def solve(s):
    seen = set()
    seen.add(s[0])
    for i in range(1, n):
        if s[i] != s[i-1] and s[i] in seen:
            return "NO"
        seen.add(s[i])
    return "YES"

for _ in range(int(input())):
    n = int(input())
    s = input()
    print(solve(s))