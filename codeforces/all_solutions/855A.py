l = set()
for _ in range(int(input())):
    s = input()
    if s in l:
        print("YES")
    else:
        print("NO")
        l.add(s)