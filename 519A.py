
m = {
    "Q": 9,
    "R": 5,
    "B": 3,
    "N": 3,
    "P": 1,
    "K": 0
}

white = black = 0
for i in range(8):
    row = input()
    for c in row:
        if c == ".": continue
        if c in "QLRBNPK":
            white += m[c]
        else:
            black += m[c.upper()]
if white < black:
    print("Black")
elif white > black:
    print("White")
else:
    print("Draw")