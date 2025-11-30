for _ in range(int(input())):
    
    l = list(map(int, input().split()))

    p1 = max(l[0], l[1])
    p2 = max(l[2], l[3])

    l.sort()
    if p1 not in l[-2:] or p2 not in l[-2:]:
        print("NO")
    else:
        print("YES")
