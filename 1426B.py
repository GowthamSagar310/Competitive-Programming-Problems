for _ in range(int(input())):
    n, m = map(int, input().split())

    """
    1. tiles are all 2x2, so odd side lengths are not possible
    2. if there is atleast one symmetric tile, we can place it all over the square
    
    """

    found_symmetric = False
    for _ in range(n):
        a, b = map(int, input().split())
        c, d = map(int, input().split())
        if b == c:
            found_symmetric = True
        
    if m % 2 == 0 and found_symmetric:
        print("YES")
    else:
        print("NO")
    