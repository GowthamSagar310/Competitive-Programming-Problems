for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    """
    - if there are duplicate values, the same is going to same for those subarray containing only that element
    - b1 + b2 + b3 .. = bk1 + bk2 + ..... bn


    log(a * b) = log(a) + log(b)
    log (a1 * a2 * a3 * a4) = log(a1) + log(a2) + .......


    log(al1 * ...... * ar1) 
    = log(al1) + ...... log(ar1)
    = bl1 log2 + ...... br1 log 2
    = log2 * (bl1 + ......... br1)

    log(al2 * ...... * ar2)
    = log2 * (bl2 + ......... br2)

    if these have to equal, 
    we just have to see if the sum of powers satisfy this or not.

    now the problem is reduced to find the two non-overlapping subarrays with same sum ? 

    if there are only unique values, and values of a are 2 ** (b), then
    - lets say a subarray is summing up to 2^6
    - we need to find if there is another subarray of values which add up to 2^6
    - since all are unique and only powers of 2
    - we can use [2^0, 2^1, 2^2, 2^4, 2^5]
    - the maximum value that can be formed these (uniquely) is 2^6 - 1.
    - so there cannot be a subarray which sums to 2^6, unless there are duplicates
    """

    if n != len(set(arr)):
        print("YES")
    else:
        print("NO")