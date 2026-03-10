illegal = False
a, b, c = 1, 2, 3
for _ in range(int(input())):
    n = int(input())
    if n == c:
        illegal = True
        print("NO")
        break
    else:
        if n == a:
            b, c = c, b
        elif n == b:
            a, c = c, a
if not illegal:
    print("YES")