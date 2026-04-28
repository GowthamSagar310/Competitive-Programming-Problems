for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    ones = s.count("1")
    zeroes = n-ones

    """
    1. n is even. 
    2. We need it be exactly k pairs
    3. if there exactly k pairs are palindromic, (n // 2) - k pairs are non-palindromic
    4. non-palindromic pairs always consists of 1 zero and 1 one. 
 


    """

    total_pairs = n // 2
    non_p = total_pairs - k

    rem_ones = ones - non_p
    rem_zeroes = zeroes - non_p

    if rem_ones >= 0 and rem_zeroes >= 0 and rem_ones % 2 == 0:
        
        # case all ones + even = possible
        # case all zeroes + even = possible
        # even zeroes + even ones = possible
        
        # the length for the palindromic pairs = even
        # so if rem_ones is odd, it wont be possible to do exactly k pairs. 
        # if rem_ones is even, rem_odds will also be even
        # because the n is even, palindromic + non-palindromic section should be even

        print("YES")
    else:
        print("NO")
