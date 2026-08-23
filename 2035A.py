for _ in range(int(input())):
    n, m, r1, c1 = map(int, input().split())
    d = 0

    # same row 
    d += (m-c1)

    # left corners
    d += (n-r1) * (m-1) # col
    d += (n-r1) # row

    # remaining 
    d += (n-r1) * (m-1) # row
    d += 0 # col

    print(d)