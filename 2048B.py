for _ in range(int(input())):
    n, k = map(int, input().split())

    """
    1 2 3 4 5 6

    1 2 3
    2 3 4
    3 4 5
    4 5 6

    most repeated = 3, 4

    if i can keep minimum values at these positions, 
    then i will get the minimum sum. 
    
    """

    mini, maxi = 1, n
    for i in range(n):
        if (i+1) % k == 0:
            print(mini, end = " ")
            mini += 1
        else:
            print(maxi, end = " ")
            maxi -= 1
    print()