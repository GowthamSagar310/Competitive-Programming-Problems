for _ in range(int(input())):
    s = input()
    ones = s.count("1")
    zeroes = len(s) - ones
    i = 0
    while i < len(s):
        l = s[i]
        if l == "0" and ones:
            ones -= 1
        elif l == "1" and zeroes:
            zeroes -= 1
        else:
            break
        i += 1
    print(len(s)-i)