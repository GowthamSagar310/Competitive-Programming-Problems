for _ in range(int(input())):
    n, m = map(int, input().split())

    """
    n x m board

    players can odd moves.

    right or up. 
    n + m - 1 tiles must be moved. 

    steps = n + m - 2 -> zero
    because the the steps are always reduced by odd, 
    the parity is going to flip after each move. 

    odd -> even -> odd -> even -> ... 0

    if steps is odd, 
    -> B is going choose some odd number
    -> now steps is even, but T cannot complete the game by choosing even, he has to choose odd. 
    -> there will always be 1 left. 
    -> B wins

    if steps is even,
    -> B choose some odd
    -> steps is now odd, T can complete the game
    
    """

    print("Burenka" if (n+m-2) & 1 else "Tonya")