for _ in range(int(input())):
    n = int(input())

    # odd number of legs - wont be possible 

    if n & 1:
        print(0)
    else:
        # count = 0
        # c = 0
        # while 2 * c <= n:
        #     rem = n - 2 * c
        #     observe that we are only count if n % 4 == 0
        #     that means 4 is constraint here, if it is 4 divisible, 
        #     then remaining can be filled with chickens
        #     the reverse is not true
        #     if rem % 4 == 0:
        #         count += 1
        #     c += 1
        # print(count)

        # number of 4 multiples <= n -> (n // 4)
        # including 0 
        #

        print((n // 4) + 1)