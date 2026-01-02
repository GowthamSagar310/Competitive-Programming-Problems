for _ in range(int(input())):
    a, b, c = map(int, input().split())

    # AP: b-a=c-b
    #     2*b = a+c
    # we can multiply "m" to one a / b/ c 
    # so after multiplying 
    # if the AP condition still holds after that, then we can convert them

    # case1: multiply a 
    # 2 * b = m * a + c
    # 2 * b - c = m * a 
    if (2 * b - c) > 0 and (2 * b - c) % a == 0:
        print("YES")


    # case2: multiply b
    # 2 * m * b = a + c
    # m = (a + c) // 2 * b
    elif (a + c) % (2 * b) == 0:
        print("YES")

    # case3: multiply c
    # 2 * b - a = m * c
    elif (2 * b - a) > 0 and (2 * b - a) % c == 0:
        print("YES")
    
    
    else:
        print("NO")
