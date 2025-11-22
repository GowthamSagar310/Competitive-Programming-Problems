def solve(s):
    c = 0
    zeros = 0
    for l in s:
        if l == '(':
            c += 1
        else:
            c -= 1
        if c == 0:
            zeros += 1
            if zeros > 1:
                return "YES"
    return "NO"


for _ in range(int(input())):
    s = input()
    print(solve(s))