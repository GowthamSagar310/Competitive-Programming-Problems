for _ in range(int(input())):
    s = input()

    # continuous 1 as one block
    # continuous 0 as one block
    # "10" needs to be cut after 1 always
    # "01" can be present once to be placed in the middle

    n = len(s)
    cuts = 0
    already_present = False
    for i in range(n-1):
        if s[i] == "1":
            if s[i+1] == "0":
                cuts += 1
        else:
            if s[i+1] == "1":
                if already_present:
                    cuts += 1
                else:
                    already_present = True

    print(cuts+1)