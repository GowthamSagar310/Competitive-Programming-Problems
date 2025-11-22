def solve(s):
    n = len(s)
    i = 1
    while i < n:
        if s[i] != s[i-1]:
            s[i], s[i-1] = s[i-1], s[i]
            return True, "".join(s)
        i += 1
    return False, ""


for _ in range(int(input())):
    s = list(input())
    result, string = solve(s)
    if result:
        print("YES")
        print(string)
    else:
        print("NO")
    