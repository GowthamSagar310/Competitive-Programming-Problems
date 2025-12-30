for _ in range(int(input())):
    s = list(input())
    ops = 0
    prev_s_index = -1
    for i, l in enumerate(s):
        if l == "s":
            prev_s_index = i
        else:
            # s is always going to be left of u
            if prev_s_index == -1:
                s[i] = "s"
                prev_s_index = i
                ops += 1
            else:
                if i+1 < len(s):
                    if s[i+1] != "s":
                        s[i+1] = "s"
                        ops += 1
                else:
                    s[i] = "s"
                    ops += 1
    print(ops)