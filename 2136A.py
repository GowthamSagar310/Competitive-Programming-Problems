from math import ceil

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())

    c, d = min(c-a, d-b), max(c-a, d-b)
    a, b = min(a, b), max(a, b)

    # for every a, are there two bs ?
    # a >= ceil(b / 2)-1
    # c >= ceil(d / 2)-1

    if a >= ceil(b/2)-1:
        if c == 0 and d == 0:
            print("YES")
        elif c >= ceil(d/2)-1:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")