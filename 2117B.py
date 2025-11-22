for _ in range(int(input())):
    n = int(input())

    # 3 
    # 2 3 1 
    
    # 4
    # 2 3 4 1
    
    # 5
    # 2 3 5 4 1

    # 6
    # 2 3 6 5 4 1

    # print("2 3 ", end = '')
    # k = n-3
    # while k > 0:
    #     print(str(n) + " ", end = '')
    #     n -= 1
    #     k -= 1
    # print("1")

    for i in range(2, n+1):
        print(str(i) + " ", end = '')
    print("1")
