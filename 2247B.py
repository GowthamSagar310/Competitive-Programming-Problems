for _ in range(int(input())):
    n, k, m = map(int, input().split())
    """
    - sum of elements of subarray % m == 0
    - minimum length of such subarray = k
    remainders 0, 1 ... m-1
    usable remainders 1 ... m-1

    - by pigeonhole principle, 
        - there are m unique remainders when dividing with "m"
        - if there are m+1 prefix sums, then one of the remainder must be repeating
        - if one of the remainder is repeated, that means the subarray between these sums, will be divisible by "m"
        - if this length < k, then there will always be a shorter subarray which will be divisible
        - the largest possible gap is just m
    """

    if k > m:
        print("NO")
    else:
        block = [1] * (k-1) + [m-k+1]
        ans = (block * ((n // k) + 1))[:n]
        print("YES")
        print(*ans)