for _ in range(int(input())):
    s = input()
    n = len(s)
    """
    s = a + b + c

    case 1: b <= a and b <= c
    case 2: b >= a and b >= c
    
    - s consits of only "a", "b"

    peti1234
    4 years ago, hide # | Add to favourites  Vote: I like it +90 Vote: I do not like it
    Easier solution for A2:

    If 𝑠[1]=𝑎, then we can split it into 𝑎=𝑠[0],𝑏=𝑠[1],𝑐=𝑠[2...𝑛−1]
    If 𝑠[1]=𝑏 ,then we can split it into 𝑎=𝑠[0],𝑏=𝑠[1....𝑛−2],𝑐=𝑠[𝑛−1].
    """

    a = s[0]
    b = s[1:-1]
    c = s[-1]

    if n == 3: print(s[0], s[1], s[2])
    elif s[0] == s[1]: print(s[0], s[1], s[2:])
    elif s[-2] == s[-1]: print(s[0:-2], s[-2], s[-1])
    else:
        if s[:2] == "ab":
            print(s[0], s[1:-1], s[-1])
        else:
            # s[:2] == "ba"
            if s[-2:] == "ab": print(s[0], s[1:-1], s[-1])
            else: print(s[0], s[1:-2], s[-2:])

            

        # "ab...ab" - s[0], s[1:-1], s[-1]
        # "ab...ba" - s[0], s[1:-1], s[-1]
        # "ba...ab" - s[0], s[1:-1], s[-1]
        # "ba...ba" - 
        """
        baba
        b a ba
        """



    # a > b and c > b - solved above
    # a > b and c < b -
    # a > b and c = b - solved above
    # a = b and c > b - solved above
    # a = b and c < b - solved above
    # a = b and c = b - solved above
    # a < b and c > b - 
    # a < b and c < b - solved above
    # a < b and c = b - solved above