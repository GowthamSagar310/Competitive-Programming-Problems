for _ in range(int(input())):
    
    k, q = map(int, input().split())
    a = list(map(int, input().split()))
    n = list(map(int, input().split()))

    # 1 <= a1 < a2 < a3 < .. <= 100
    # for num in n:
    #     i = k-1
    #     length = num
    #     ops = 0
    #     while i >= 0:
    #         while length >= a[i]:
    #             length -= (i+1)
    #             ops += (i+1)
    #         i -= 1
    #     print(num-ops, end=" ")
    # print()

    for num in n:
        print(min(num, a[0]-1), end=" ")
    print()