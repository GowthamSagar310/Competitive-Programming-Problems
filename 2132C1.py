from math import log
for _ in range(int(input())):
    n = int(input())

    """
    - sells 3^x for 3^(x+1) + x. 3^(x-1) coins
    - buyer wants to buy n watermelons, while making the least possible number of deals
    - 
    
    x = 0 -> 1 watermelon = 3 coins = 3per watermelon
    x = 1 -> 3 watermelons for 9 + 1 * 1 = 10 coins = 3.33 per watermelon
    x = 2 -> 6 watermelons for 27 + 6 = 33 coins = 5.5 per watermelon
    
    - the cost per watermelon is increasing. 
    - we are optimizing for the least possible number of deals, not the cost
    
    3^x <= n

    max_n = 10**9

    = log3(10**9)
    = 9 * log3(9)
    ~ 18
    """

    cost = 0 
    powers = []
    for i in range(21):
        powers.append(3 ** i)
    while n:
        for i in range(20, -1, -1):
            val = powers[i]
            if val <= n:
                n -= val
                cost += int(3 ** (i+1) + i * (3 ** (i-1)))
                break
    print(cost)