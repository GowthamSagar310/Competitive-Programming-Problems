for _ in range(int(input())):
    n = int(input())
    a = input()
    l = int(input())
    b = input()
    c = input()

    for i in range(l):
        if c[i] == "D":
            a = a + b[i]
        else:
            a = b[i] + a

    print(a)

    # we can do this by taking a sufficiently large array, updating and then joining at end.