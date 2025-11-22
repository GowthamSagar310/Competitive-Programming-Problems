for _ in range(int(input())):
    n = int(input())
    s = input()

    res = [""] * (n)
    back, front = n, 1
    for i in range(len(s)-1, -1, -1):
        if s[i] == ">":
            # i+1 pos, should be larger than everything before
            res[i+1] = str(back)
            back -= 1
        else:
            res[i+1] = str(front)
            front += 1
    print(str(back) + " ".join(res))