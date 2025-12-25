def comp(a, b):
    if a > b: return 1
    if a == b: return 0
    if a < b: return -1

for _ in range(int(input())):
    a1, a2, b1, b2 = map(int, input().split())

    # wins = 0

    # if a1 > b1 and a2 >= b2: wins += 1
    # if a1 > b2 and a2 >= b1: wins += 1
    # if a2 > b1 and a1 >= b2: wins += 1
    # if a2 > b2 and a1 >= b1: wins += 1
    # if b1 == a1 and a2 > b2: wins += 1
    # if b1 == a2 and a1 > b2: wins += 1
    # if b2 == a1 and a2 > b1: wins += 1
    # if b2 == a2 and a1 > b1: wins += 1

    # print(wins)

    wins = 0

    if comp(a1, b1) + comp(a2, b2) > 0:
        wins += 1
    
    if comp(a1, b2) + comp(a2, b1) > 0:
        wins += 1
    
    if comp(a2, b1) + comp(a1, b2) > 0:
        wins += 1
    
    if comp(a2, b2) + comp(a1, b1) > 0:
        wins += 1
    
    print(wins)