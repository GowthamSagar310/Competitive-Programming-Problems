for _ in range(int(input())):
    r, x, d, n = map(int, input().split())
    s = input()

    # initial rating = r
    # for "1" -> no need to change rating,
    # but it is always optimal to reduce the rating
    # so that in future, we might attend div 2 
    # so, max(0, r-x)

    attends = 0
    for contest in s:
        if contest == "1" or (contest == "2" and r < x):
            attends += 1
            r = max(0, r-d)
    print(attends)