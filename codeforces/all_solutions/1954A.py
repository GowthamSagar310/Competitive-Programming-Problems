for _ in range(int(input())):
    n, m, k = map(int, input().split())
    
    # m -> types of colours
    # k -> number of moves for bob to change
    # they cannot be compared directly

    # the intuition here is, 
    # if most repeating colour in ribbon (after alice paints)
    # repeats for n-k times, the reamining k can be changed. -> so bob wins
    # so alice has to paint such that, 
    # the most repeating colour frequency is n-k-1

    # if n-k-1 <= 0:
    #     print("NO")
    # else:
    #     # if each colour is repeated n-k-1 times or less
    #     # it should be possible for alice
        # if m * (n-k-1) >= n:
        #     print("YES")
        # else:
        #     print("NO")

    # simplified
    # if n-k-1 is <= 0, m * (n-k+1) <= 0, but n > 0
    # so

    if m * (n-k-1) >= n:
        print("YES")
    else:
        print("NO")
