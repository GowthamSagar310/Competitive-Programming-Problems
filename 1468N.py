for _ in range(int(input())):
    c1, c2, c3 = map(int, input().split())
    a1, a2, a3, a4, a5 = map(int, input().split())

    c1 -= a1
    c2 -= a2
    c3 -= a3

    if c1 < 0 or c2 < 0 or c3 < 0:
        print("NO")
    else:
        # c1 + c3 >= a4
        # c2 + c3 >= a5

        if c1 + c3 >= a4:
            diff = min(c1, a4)
            c1 -= diff
            a4 -= diff
            c3 -= a4
            if c3 < 0:
                print("NO")
            else:
                if c2 + c3 >= a5:
                    diff = min(c2, a5)
                    c2 -= diff
                    a5 -= diff
                    c3 -= a5
                    if c3 < 0:
                        print("NO")
                    else:
                        print("YES")
                else:
                    print("NO")
        else:
            print("NO")