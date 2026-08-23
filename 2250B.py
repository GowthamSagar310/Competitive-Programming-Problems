for _ in range(int(input())):
    n, k = map(int, input().split())

    """
    - string length is n
    - there should be "exactly" k pairs of adjacent elements which have same value
    - difference between number of 0s and 1s is atmost 1

    - for even length is possible to get difference as 1
    - x = number of 1s, y = number of 0s
    - x + y = even
    - odd, odd or even, even
    - their difference is always > 1
    - so x == y in case of even length

    - for odd length
    - x + y = odd 
    - (odd, even) -> x != y
    - difference between odd and even >= 1
    - since atmost 1 is the difference abs(x-y) = 1


    n = 7 k = 0  0101010
    n = 7 k = 1  1101010
    n = 7 k = 2  1100101
    n = 7 k = 3  1100101
    n = 7 k = 4  1110001
    n = 7 k = 5  1111000

    n = 6 k = 0  010101
    n = 6 k = 1  110101
    n = 6 k = 2  110010
    n = 6 k = 3  111001
    n = 6 k = 4  111000
    """

    if k == n-1:
        print(-1)
    elif k == 0:
        print(("01" * ((n+1) // 2))[:n])
    else:
        """
        ones = n//2 + (1 if odd else 0)
        zeroes = n//2


        n = 6 k = 1 011010
        n = 6 k = 2 011001
        


        
        """