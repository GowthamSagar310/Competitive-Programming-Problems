for _ in range(int(input())):
    n = int(input())

    # if n % 3 == 0:
    #     print(n//3, 0, 0)
    # elif n % 3 == 1:
    #     k = n // 3
    #     if k >= 2:
    #         print(k-2, 0, 1)
    #     else:
    #         print(-1)
    # else:
    #     k = n // 3
    #     if k >= 1:
    #         print(k-1, 1, 0)
    #     else:
    #         print(-1)

    if n == 1 or n == 2 or n == 4:
        print(-1)
    else:
        if n % 3 == 0:
            print(n//3, 0, 0)
        elif n % 3 == 1:
            print((n-7)//3, 0, 1)
        else:
            print((n-5)//3, 1, 0)