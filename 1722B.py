def solve(s1, s2):
    for l1, l2 in zip(s1, s2):
        if (l1 == "R" and l2 != "R") or (l2 == "R" and l1 != "R"):
            return "NO"
    return "YES"

for _ in range(int(input())):
    n = int(input())
    s1, s2 = input(), input()
    print(solve(s1, s2))