for _ in range(int(input())):
    a, b, x = map(int, input().split())

    """
    - make a == b

    - op1: add 1 to a / b
    - op2: divide a or b by x. floor.
    
    1 2 3  op1 
    2 3 2  op1
    7 3 10 
    4 op1 or 2 op2 to make both 0

    17 3 3
    1op2 + 2op1

    17 3 3 14
    5 3 3   2
    """
    # def recur(a, b, ops):
    #     if a == b: return ops
    #     ans = ops + abs(a-b)
    #     if a > b:
    #         ans = min(ans, recur(a // x, b, ops + 1))
    #     else:
    #         ans = min(ans, recur(a, b // x, ops + 1))
    #     return ans
    # print(recur(a, b, 0))


    """
    p = kx + r 
    0 <= r < x
    
    case 1: r < x-1
    if we first add +1 and then try to divide
    p+1 = kx+r+1
    r < x-1
    r+1 < x
    floor(p+1 / x) = k = floor(p/x) = that means +1 and then dividing with x has no effect. it is same as dividing directly

    case2: r = x-1
    p+1 = kx + r-1
    p+1=  kx + x
    floor(p+1 / x) = k + 1 = floor(p/x) + 1 = that means +1 and then dividing is same as dividing and then adding 1
    
    so even if we keep dividing until we can and then look at the difference
    or add, divide, add randomly and appropriately -> it should take the same steps only

    since dividing is easy to do first, we can choose dividing and then adding necessarily should give the same answer
    """
    divison_already = 0
    ans = float("inf")
    while a != b:
        if a > b: a, b = b, a
        ans = min(ans, divison_already + b-a)
        b //= x
        divison_already += 1
    
    # why take min(ans, divison_already) ? why not ans is already final ? 
    # because we are calculating divisions only after calculating the answer. we are dividing after setting the ans.
    # the divided value is only used in the next iteration. 
    # if after two iterations both values become zero (bceause of divisons), but then difference is more. we would not have change to set the value of ans to minimum. because the loop is terminated. 

    # ans = min(ans, divison_already + b-a)
    # here b == a, so essentially 
    # ans = min(ans, division_already)
    
    print(min(ans, divison_already))