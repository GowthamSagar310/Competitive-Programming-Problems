for _ in range(int(input())):
    n = int(input())
    s = list(input())
    i = 0
    count = 0
    ops = 0
    while i < len(s):
        count += 1 if s[i] == "(" else -1
        if count < 0:
            s.append(s[i])
            count += 1
            ops += 1
        i += 1
    print(ops)