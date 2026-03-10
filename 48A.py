m = {
    "rock": "R",
    "scissors": "S",
    "paper": "P"
}
F = m[input()]
M = m[input()]
S = m[input()]

valid = ["PRR","RPR","RRP","SPP","PSP","PPS","RSS","SRS","SSR"]
if (F + M + S) in valid:
    if F == M: print("S")
    elif F == S: print("M")
    else:
        print("F")
else:
    print("?")