for _ in range(int(input())):
    m, a, b, c = map(int, input().split())
    row1 = row2 = m
    
    # a's preferences
    total = min(a, row1)
    row1 -= min(a, row1)

    # b's preferences
    total += min(b, row2)
    row2 -= min(b, row2)

    # c's preferences
    remaining_seats = row1 + row2
    total += min(c, row1 + row2)

    print(total)
