for _ in range(int(input())):
    n = int(input())

    # distinct positive integers

    # a + b + c = n
    # gcd(a, b) = c
    # a % c = 0
    # b % c = 0

    if n % 2 == 0:
        # print((n // 2)-1, n // 2, 1)
        # n is even
        # n - 3 must be odd
        # gcd(n-3, 2) = gcd(odd, 2) = 1
        print(n-3, 2, 1)
    else:
        # n = odd
        
        # e + e + o
        # this cannot be possible because
        # gcd(even, even) wont be an odd number

        # o + o + e
        # this cannot be possible

        # e + o + e
        # this cannot be possible 

        # o + e + o
        # this cannot be possible

        # o + o + o
        # this is possible 

        # say c = 1, meaning gcd(a, b) = 1
        if ((n - 1) // 2) % 2 == 0:
            # each half is even, but we need them to be odd.
            # let s = n-1
            # let a = (s/2)-1
            # let b = (s/2)+1
            # gcd(a, b) = gcd(s/2-1,s/2+1)
            # gcd(a, b-a) = gcd(s/2-1, 2) = gcd(a, 2) = gcd(odd, 2) = 1
            
            s = n-1
            a = (s // 2)-1
            b = (s // 2)+1

            print(a, b, 1)
        else:
            # each half is odd, we need them odd but different
            # let s = n-1 (even)
            # let a = (s/2)-2 (odd-even=odd)
            # let b = (s/2)+2 (odd+even=odd)
            # gcd(a, b) = gcd(s/2-2, s/2+2)
            # gcd(a, b-a) = gcd(s/2-2, 4) = gcd(a, 4) = gcd(odd, 4) = 1

            s = n-1
            a = (s // 2)-2
            b = (s // 2)+2

            print(a, b, 1)


    # if S is divisible 4, then S / 2 is always even
    # how ? 
    # S = 4 * k (k can be 0, 1, 2 .. )
    # S/ 2 = 2 * k = 2 * something = always even

    # so instead of checking ((n-1)//2) % 2 == 0
    # we can simply check if (n-1)%4 == 0