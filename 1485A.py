for _ in range(int(input())):
    a, b = map(int, input().split())
    if a < b:
        print(1)
    elif a == b:
        print(2)
    else:

        # if b == 1, we cannot reduce a, so b += 1, ops = 1
        # if b == 2, this is going to take the maximum divisions
        # O(loga base 2)
        # max number = 10**9 = O(log 10** 9) ~= log (2 ** 30)
        # max number =~ 30 divisions are enough. 
        # b > 2, is always going take less the 30 divisons

        """
        - how do you mathematically decide which operation to take ? 
        
        - our objective is reduce "a" to 0 
            - in case of a > b, is it better to first increase the value of b such that b > a, and then reduce a to 0
            - or use operation 1 -> a // b, to reduce "a"

            logb(n) = x
            b^x = n
            x * log(b) = log(n)

            logb+1(n) = y
            (b+1)^y = n
            y * log(b+1) = log(n)
            y * log(b+1) = x * log(b)
            y = x * (log b) / (log(b+1))

            b < b+1
            log(b) < log(b+1)
            y = x * (less than 0)
            
            y is always smaller
        """

        # # a > b
        # for k in range(2, a+2):
        #     ops = k-b
        #     temp = a 
        #     while temp:
        #         ops += 1
        #         temp //= k
        #     print(a, k, ops)

        min_ops = float("inf")
        for k in range(b, b+31):
            ops = k-b
            if k == 1: k += 1; ops += 1
            temp = a
            while temp:
                ops += 1
                temp //= k
            min_ops = min(min_ops, ops)
        print(min_ops)
