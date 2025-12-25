for r in range(1, 6):
    row = input().split()
    found = False
    for c in range(1, 6):
        if row[c-1] == "1":
            found = True
            print(abs(c-3) + abs(r-3))
    if found: break
