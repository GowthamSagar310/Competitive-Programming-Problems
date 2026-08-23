"""
- the idea here is to think of it like a chess board
- filled with white and black cells (which is like parity (x+y) % 2)
- it going to be either 0/1 and is always alternating 
- if the parity of friend and vika are equal, (both in black or both white cells)
- they are diagonal (if next to each other), and vika cannot run
"""
for _ in range(int(input())):
    n, m, k = map(int, input().split())
    xv, yv = map(int, input().split())
    parity = (xv + yv) % 2
    friends = []
    for _ in range(k):
        x, y = map(int, input().split())
        friends.append((x, y))
    caught = False
    for x, y in friends:
        if (x + y) % 2 == parity:
            caught = True
            break
    print("NO" if caught else "YES")
