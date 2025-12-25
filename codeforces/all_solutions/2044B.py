for _ in range(int(input())):
    s = input()
    res = []
    for i in range(len(s)-1, -1, -1):
        if s[i] == "p":
            res.append("q")
        elif s[i] == "q":
            res.append("p")
        else:
            res.append("w")
    print("".join(res))
