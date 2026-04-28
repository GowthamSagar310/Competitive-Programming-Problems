for _ in range(int(input())):
    a, b, c, d = map(int, input().split())

    """
    a/ b =  c/d
    
    a   c
    - = -
    b   d

    100 3 25 6

    200 / 6 = 25 / 6


    """ 

    if a/b == c/d:
        print(0)
    elif a * b * c == c / d or a * b * c == a / b:
        print(1)
    else:
        print(2)

