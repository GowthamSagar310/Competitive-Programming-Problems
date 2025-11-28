for _ in range(int(input())):
    a, b, x, y = map(int, input().split())

    # make a = b
    # by applying operations on a
    # op1 -> a = a + 1 costs x
    # op2 -> a = a ^ 1 costs y

    # a 0001001
    # a ^ 1 = 0001000
    # a ^ 1 = 0001001

    if a % 2 == 1 and a - b == 1:
        print(y)
    elif a > b:
        print(-1)
    elif a == b:
        print(0)
    else:
        difference = b - a
        if x <= y:
            print(difference * x)
        else:

            # 1 2 3 4 5 6 
            # diff = 5
            # x y x y x 

            # 1 2 3 4 5 6 7
            # diff = 6
            # x y x y x y

            # 2 3 4 5 6
            # diff = 4
            # y x y x

            # 2 3 4 5 6 7
            # diff = 5
            # y x y x y

            a_even = a % 2 == 0
            if a_even:
                print(y * ((difference + 1) // 2) + x * (difference // 2))
            else:
                print(x * ((difference + 1) // 2) + y * (difference // 2))