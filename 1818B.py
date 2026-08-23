for _ in range(int(input())):
    n = int(input())

    """

    consider swapping adjacent elemtns of permutation
    - [2, 1, 4, 3, 6, 5, ....]

    - since this is permuatation, we should also think in terms of arithmetic progression
    - for AP, the sum is (L)(l+r)/2
    - if the subarray first element is l, and last is r
    - and L = length of the subrray = number of elements = r-l+1
 
    - if L is odd, 
        - S % L -> (l+r)/2 
            - for odd lengthed subarrays, (l+r) is even
            - so (l+r) / 2 is divisible
        - so there is no answer if L is odd (except for L = 1, as l < r)
    - if L is even, there can be an answer. 

    - [2, 1, 4, 3, 6, 5, ...]
    - for L = 2, the sum is always odd, so this pattern works
    - but for L = 3, 4, ... ? how to prove ?

    - S = Sum of progression + S of delta 
    - here the delta are because the values are changed by +1 or -1

    - for L = even L >= 2
    - the delta is 0. 
    - S = L(l+r)/2
    - S/L = (l+r)/2 = odd/2 which is never divisible

    - for L = odd L >= 3
    - the delta is +1 / -1
    - S = L(l+r)/2 + (delta)
    - S/L = (l+r)/2 + delta/L
    - S/L = integer + delta/L
    - which is not integer, so not divisible. 
    - for all the cases, this pattern is not divisible

    """

    if n == 1:
        print(1)
        continue

    if n % 2:
        print(-1)
        continue

    ans = list(range(1, n+1))
    for i in range(n):
        ans[i] += (-1) ** (i)
    
    print(*ans)
