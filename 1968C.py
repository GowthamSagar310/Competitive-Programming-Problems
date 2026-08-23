from math import ceil
for _ in range(int(input())):
    n = int(input())
    """
    _ 2 4 1
    3 5 4 5 
    
    _ 1 1
    2 3 4

           r1   r2
    _ 4 2  5 1 100
          a1 a2 a3

    a2 > r2
    a1 * k + r1 > r2
    a1 * k > r2 - r1
    k > ceil((r2 - r1) / a1)

    """
    # remainders = list(map(int, input().split()))
    # ans = [remainders[0]+1]
    # for i in range(n-2):
    #     r1 = remainders[i]
    #     a1 = ans[-1]
    #     r2 = remainders[i+1]
    #     k = max(0, ceil((r2-r1)/ a1)+1)
    #     a2 = a1 * k + r1
    #     ans.append(a2)
    # ans.append(remainders[-1])
    # new_x = [ans[i] % ans[i-1] for i in range(1, n)]
    # print(ans, remainders == new_x)
    # print(*ans)

    """
    since the maximum value of x is 500, 
    if a1 = 501
    then a2, can be a1 + r, here r is less than 501
    then a3, can be a2 + r, again r is less than 501
    """


    remainders = list(map(int, input().split()))
    ans = [501]
    for i in range(n-1):
        ans.append(ans[-1] + remainders[i])
    # new_x = [ans[i] % ans[i-1] for i in range(1, n)]
    # print(ans, remainders == new_x)
    print(*ans)

