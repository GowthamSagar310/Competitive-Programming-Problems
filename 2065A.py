for _ in range(int(input())):
    s = list(input())
    s[-1] = ""
    s[-2] = "i"
    print("".join(s))
    