for _ in range(int(input())):
    n = int(input())

    # need to replace n tires
    # 4 wheels or 6 wheels
    # 

    # if n & 1 or n < 4:
    #     print(-1)
    # else:
    #     # # maximum number of buses
    #     # # remaining can be 0,1,2,3 wheels
    #     # # if remainder = 0 -> 0 6 wheels buses
    #     # # if remainder = 1 -> not possible
    #     # # if remainder = 2 -> convert 1 4 to 6
    #     # # if remainder = 3 -> not possible

    #     max_four_wheels = n // 4
    #     remainder = n % 4
    #     if remainder == 0:
    #         maxi = max_four_wheels
    #     elif remainder == 2:
    #         maxi = max_four_wheels-1+1
    #     else:
    #         maxi = -1
        
    #     # # minimum number of buses
    #     # # use 6 wheels more
    #     max_six_wheels = n // 6
    #     remainder = n % 6

    #     # # r = 0 -> max_six_wheels
    #     # # r = 1 -> not possible
    #     # # r = 2 -> use 1 6 to 2 4
    #     # # r = 3 -> not possible
    #     # # r = 4 -> use 2 6 to 2 4
    #     # # r = 5 -> not possible 

    #     if remainder == 0:
    #         mini = max_six_wheels
    #     elif remainder == 2:
    #         mini = max_six_wheels-1+2
    #     elif remainder == 4:
    #         mini = max_six_wheels+1
    #     else:
    #         mini = -1

    #     print(f"{mini} {maxi}")


    if n & 1 or n < 4:
        print(-1)
    else:
        maximum = n // 4
        minimum = (n+6-1) // 6

        # we are using ceil for minimum because
        # we can convert one of the 6 to 2 4fours i.e (-1+2) = +1 
        # (or) if remainder = 4, that can be converted 1four, i.e (+1) = +1

        # we are not using ceil for maximum because
        # remainders possible for 4 are 0, 1, 2, 3
        # 0 -> cannot convert to 6
        # 1, 3 -> not possible
        # 2 -> convert 1 4 to 1 6 (+1-1) = 0 (no extra)
        print(f"{minimum} {maximum}")

