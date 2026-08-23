for _ in range(int(input())):
    s = input()
    n = len(s)
    ans = "-1"
    for i in range(n-1):
        if len(set(s[i:i+2])) == 1:
            ans = s[i:i+2]
            break
        if len(set(s[i:i+3])) == 3:
            ans = s[i:i+3]
            break
    print(ans)

    """
    a b c
    ab bc
    abc 

    aa
    a aa
    """

        