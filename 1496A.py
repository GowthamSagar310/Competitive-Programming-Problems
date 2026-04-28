for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    """
    
    we have to make k+1 parts.
    last part if not reversible. 
    so,  

    if n is even -> ak+1 should be even
    if n is odd -> ak+1 should be odd



    all the other parts must be palindromes
    
    """

    count = 0
    l, r = 0, n-1
    while l < (n-1) // 2:
        if s[l] == s[r]:
            count += 1
        else:
            # if we it is not palindrome anymore, we cannot break it. 
            # so stop.
            break
        l += 1
        r -= 1
    
    if count >= k:
        print("YES")
    else:
        print("NO")
