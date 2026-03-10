for _ in range(int(input())):
    n, k, x = map(int, input().split())

    # if x != 1:
    #     print("YES")
    #     print(n)
    #     print(*[1] * n)
    
    # elif k == 1:

    #     # x == 1 and k == 1
    #     # there are no other numbers

    #     print("NO")
    
    # elif k == 2:
    #     if n % 2 == 0:
    #         print("YES")
    #         print(n // 2)
    #         print(*[2] * (n // 2))
    #     else:
    #         print("NO")
    
    # else:

    #     # k >= 3
    #     # x == 1
    #     if n == 1:
    #         # this case is useless to write because
    # 
    #         print("NO")
    #     elif n % 2 == 0:
    #         print("YES")
    #         print(n // 2)
    #         print(*[2] * (n // 2))
    #     else:
    #         print("YES")
    #         num_twos = (n-3) // 2
            # print(num_twos + 1)
            # print(3, *[2] * num_twos)


    # SIMPLER
    if x != 1:
        print("YES")
        print(n)
        print(*[1] * n)
    elif k == 1 or (k == 2 and n & 1):
        print("NO")
    else:
        print("YES")
        print(n//2)
        print(3 if n %2==1 else 2, *[2]*((n//2) -1))
        
