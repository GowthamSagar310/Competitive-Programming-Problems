for _ in range(int(input())):
    n, k = map(int, input().split())

    """
    (a1, a2, a3, a4 ... an) / k
    1. either each one of them is divisible by k
    2. the sum of remainders is divisible by k
    3. a1 + a2 + a3 ... an >= k

    1, 2, .... k-1
    1 + (k-1)
    2 + (k-2)
    ..
    all these pairs are divisible by k
    
    4 3
    1 2 1 2

    8 17
    """

