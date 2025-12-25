for _ in range(int(input())):
    n = int(input())
    for i in range(1, n+1):

        # this needs to be satisfied over all the pairs
        # a1 mod 1 != a2 mod 2
        # a1 < a2
        # 1 <= a1 < a2 <= 100
        
        # if i have to get mod 0 with 1, i need 1
        # if i have to get mod 1 with 2, i need 3
        # if i have to get mod 2 with 3, i need 5
        # if i have to get mod 3 with 4, i need 7
        # 1 -> 1 
        # 2 -> 3
        # 3 -> 5
        # 50 -> 99 
        # n -> 2*n-1

        print(2 * i - 1, end = " ")
    print()
    


