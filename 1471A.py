for _ in range(int(input())):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    # if val is divisible by x => maximum beauty that can be extracted is always val // x
    # this cannot be increased
    # remainder 1 to x-1 are going to give extra 1 to the ceil value
    # for maximum, we need to leave them as is
    # so for minimum value, we need to mix the values such that they are divisible by x

    # current_total = 0
    # current_r = 0
    # maxi = mini = 0
    # for val in arr:
    #     maxi += (val + x - 1) // x
    #     if (current_total + val) % x == 0:
    #         mini += (current_total + val) // x
    #         current_total = 0
    #     else:
    #         current_total += val
    # if current_total: mini += (current_total + x - 1) // x
    # print(f"{mini} {maxi}")

    # simpler solution
    # ceil((a+b) / x) <= ceil(a/x) + ceil(b/x)
    # because both individually can contribute 1 on right side
    # but by adding, it either produces 1 extra if a+b is not divisible
    # but if divisible, it produces none
    
    # in above implementation, I took subarrays which are divisible by x
    # but this is useless the total sum when MOD by x, 
    # the answer does not change. 
    # that is to say, 
    # if there are two groups which are divisible by x -> answer would not change by combining them
    # if there are two groups which are not divisible by x -> treating them combinedly would not change the combined remainder
    total = 0
    maxi = 0
    for val in arr:
        maxi += (val + x - 1) // x
        total += val
    print(f"{(total + x - 1) // x} {maxi}")