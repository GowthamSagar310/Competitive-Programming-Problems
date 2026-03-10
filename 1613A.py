import math
for _ in range(int(input())):
    x1, p1 = map(int, input().split())
    x2, p2 = map(int, input().split())

    # precision errors
    # a = math.log10(x1) + p1
    # b = math.log10(x2) + p2
    # if a < b: print("<")
    # elif a == b: print("=")
    # else: print(">")

    # if a < b, then for a positive number k
    # (a/k) < (b/k) -> the sign does not change

    # so if we can remove the common zeros
    # between the two numbers, 
    # it does not change the answer
    
    p = min(p1, p2)
    p1 -= p
    p2 -= p
    
    # either p1 or p2 will now become 0
    # and only x is remained
    # given that x <= 10^6 that 7 digit number
    
    # so if p1 >= 7, regardless of x1, this is greater

    if p1 >= 7:
        print(">")
    elif p2 >= 7:
        print("<")
    else:
        # p1 == 0 and p2 < 7
        # p2 == 0 and p1 < 7

        val1 = x1 * (10 ** p1)
        val2 = x2 * (10 ** p2)

        if val1 < val2:
            print("<")
        elif val1 > val2:
            print(">")
        else:
            print("=")