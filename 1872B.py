for _ in range(int(input())):
    n = int(input())
    maxi = float("inf")
    for _ in range(n):    
        d, s = map(int, input().split())
        maxi = min(maxi, d + (s - 1) // 2)
    print(maxi)

    """
    so the trap in current room is allowing you to move to some rooms and comeback. 
    we have to be in each room, just before the trap is activated. 
    from the current time, there are si seconds for the trap to get activated. 
    so in si seconds, how far can you go and come back just before the trap is activated ? 
    d + (s-1) // 2
    """

