for _ in range(int(input())):
    s = input()
    if s[0] == "0":
        print("0")
    else:
        count = 1
        for i, l in enumerate(s):
            if l == "?":
                if i == 0:
                    count *= 9
                else:
                    count *= 10
        print(count)
