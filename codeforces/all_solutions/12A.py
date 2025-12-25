row1 = input()
row2 = input()
row3 = input()

symmetric = all([
    row1[0] == row3[2],
    row1[1] == row3[1],
    row1[2] == row3[0],
    row2[0] == row2[2]
])

print("YES" if symmetric else "NO")