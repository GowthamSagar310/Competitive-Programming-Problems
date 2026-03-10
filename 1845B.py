for _ in range(int(input())):
    xa, ya = map(int, input().split())
    xb, yb = map(int, input().split())
    xc, yc = map(int, input().split())


    # if xa is in middle of xb and xc, there is only one
    # but if xb, xc are both < or > than xa
    # then abs(min(xb, xc)-xa)+1
    # same with y direction

    shared_steps = 0

    # x direction
    diff_b = xb - xa
    diff_c = xc - xa
    if (diff_b > 0 and diff_c > 0) or (diff_b < 0 and diff_c < 0):
        shared_steps += min(abs(diff_b), abs(diff_c))

    diff_b = yb-ya
    diff_c = yc-ya
    if (diff_b > 0 and diff_c > 0) or (diff_b < 0 and diff_c < 0):
        shared_steps += min(abs(diff_b), abs(diff_c))

    print(shared_steps + 1)    