for _ in range(int(input())):
    s = input()
    # if len(set(s)) == 1:
    #     print(-1)
    # else:
    #     print("".join(sorted(s)))
    
    ss = sorted(s)
    if ss[0] == ss[-1]:
        print(-1)
    else:
        print("".join(ss))