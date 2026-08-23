for _ in range(int(input())):
    n, k = map(int, input().split())


    """
    - A -> x = n (n >= 0)
    - find B, such that abs(OB - AB) = k
    - OB-AB = k
    - AB-OB = k
    """
    if n <= k:
        print(k-n)
    else:
        if (n-k) % 2 == 0:
            print(0)
        else:
            print(1)