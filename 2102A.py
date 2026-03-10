for _ in range(int(input())):
    n, m, p, q = map(int, input().split())

    # i am thinking in terms of 0, 1
    # but what if m > n ? 

    # what if all elements are equal ? 
    # so all subarrays of length p will have same sum
    # but it should be equal to q

    """
    n = 3 m = 2 p = 2 q = 1
    0 1 0

    n = 1 m = 1 p = 1 q = 1
    1 

    n = 5 m = 4 p = 2

    1. if the first p elements are determined, 
       I can just use the same again and again
       e.g 1 2 3 1 2 3 ....

    2. if n % p == 0, that means there are n//p subarrays
       meaning, (n // p) * q is the total sum
       if this is equal to "m", then somehow it is possible to do this. 
       if this is not equal to "m", that means array cannot be made. 

    3. if n % p != 0, that means there are n//p subarrays + 1 unfinished block
       say p = 3, n = 7 m = 10 q = 3
       A B C A B C A = 10
       2 * (A B C) + A = 10
       2 * (3) + A = 10
       A = 4

       since, A = 4
       A + B + C = 3
       B + C = -1

       B + C can be anything 
       1, -2
       6, -7 
       etc.

       4 1 -2 4 1 -2 4 = 10

       this is because we can choose any number, all positive can be balanced by some negatives

       if this remainder is not present, (n // p) * m should exactly divisible
    """

    if n % p == 0 and (n // p) * q != m:
        print("NO")
    else:
        print("YES")