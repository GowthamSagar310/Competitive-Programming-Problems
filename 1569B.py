for _ in range(int(input())):
    n = int(input())
    s = input()

    """
    type1: zero losses
    type2: atleast 1 win
    """

    twos = []
    for i, c in enumerate(s): 
        if c == "2":
            twos.append(i)

    if not twos or len(twos) >= 3:
        print("YES")
        
        grid = [["" for _ in range(n)] for _ in range(n)]
        for i in range(len(twos)):
            f, s = i, i+1 if i+1 < len(twos) else 0
            p1, p2 = twos[f], twos[s]
            grid[p1][p2] = "+"
            grid[p2][p1] = "-"
        
        for i in range(n):
            for j in range(n):
                if i == j:
                    grid[i][j] = "X"
                elif grid[i][j] == "":
                    grid[i][j] = "="
        
        for row in grid:
            print("".join(row))

    else:
        print("NO")
