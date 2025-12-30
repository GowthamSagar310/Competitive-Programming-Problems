for _ in range(int(input())):
    
    i,j = map(int, input().split())
    row = max(i, j)
    maxi = row ** 2
    mini = ((row-1) ** 2) + 1

    if row & 1:
        # small to big
        if j <= i:
            print(mini + (j-1))
        else:
            print(maxi - (i-1))
    else:
        # big to small
        if j <= i:
            print(maxi - (j-1))
        else:
            print(mini + (i-1))
        