for _ in range(int(input())):
    a, b = map(int, input().split())

    """
    step 1 exchange the wallets or keep the wallet
    step 2 remove one coin from player's wallet

    a == b
    a < b
    a > b

    1. the total sum of the value is reduced 1 always
    2. a move can always be made if there is coin. 

    sum -> 0
    odd sum made to zero -> in odd moves (alice always has a move)
    even sum made to zero -> even moves (bob always has a move)
    """

    print("Alice" if (a + b) & 1 else "Bob")