def solve(s, n):
    reference = "meow"
    i = j = 0
    while i < n:
        if j < 4 and s[i].lower() == reference[j]:
            while i < n and s[i].lower() == reference[j]:
                i += 1
            j += 1
        else:
            return "NO"
    return "YES" if j == 4 else "NO"

for _ in range(int(input())):
    n = int(input())
    s = input()
    print(solve(s, n))

