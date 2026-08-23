for _ in range(int(input())):
    x, y = map(int, input().split())
    
    """
    - S(n) = x
    - S(n+1) = y

    how can the sum of n and n+1 change ?
    1234, 1235 d = 1
    1239, 1240 d = 8
    1299, 1300 d = 17
    1999, 2000 d = 26
   9999, 10000 d = 35
    """

    if x == y:
        print("NO")
    elif x < y:
        # there cannot be a 9 in this number at the end
        # so difference between y and x must be 1
        print("YES" if y-x == 1 else "NO")
    else:
        # x is greater than y
        # that means adding 1 to the number n, is decreasing the value 
        # there must be a 9 present. 
        if (x-y+1) % 9 == 0:
            print("YES")
        else:
            print("NO")