for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    # gcd >= 3
    # gcd(a, b) >= min(a, b) >= 3

    # so the sum of these values must be >= 3

    # it is a very clever idea to 
    # make every element equal to some value x and make sure that x >= 3
    # 
    # 1   2   3 4 5 6 .... n-1, n 
    # n n-1 n-2 . .........  2, 1
    # 
    # sum of each of these will be n+1

    # and because n >= 2
    # n+1 >= 3 
    # so gcd of adjacent pairs will always be >= 3

    for val in arr:
        print((n+1)-val, end = " ")
    print()
    