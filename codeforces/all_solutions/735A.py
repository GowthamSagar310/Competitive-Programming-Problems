def solve(s):
    g_index = s.index("G")
    t_index = s.index("T")

    diff = abs(g_index - t_index)
    if diff % k != 0:
        return "NO"

    for i in range(g_index, t_index+(1 if g_index < t_index else -1), k if g_index < t_index else -k):
        if i == t_index:
            return "YES"
        elif s[i] == "#":
            return "NO"
    return "NO"

n, k = map(int, input().split())
s = input()
print(solve(s))