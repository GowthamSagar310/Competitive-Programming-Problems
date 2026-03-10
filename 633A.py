from math import gcd
a, b, c = map(int, input().split())

g = gcd(a, b)
if c % g != 0:
    # with c is not divisible by g, then it is not possible
    print("No")
else:
    # if c % g == 0, then there might be a solution

    # Forbenius limit
    # if a, b are coprimes (gcd=1)
    # then the largest number that is not possible to make is a*b-a-b
    # anything about this can be made. 
    # anything below this, we need to check manualy. there are only few numbers which are possible.


    limit = a * b - a - b
    if c > limit:
        print("Yes")
    else:
        flag = False
        for i in range(c+1):
            if (c - i * a) >= 0 and (c - i * a) %  b == 0:
                flag = True
                print("Yes")
                break

        if not flag: 
            print("No")


    # ax + by = c
    # this is has a integral solution only if c % gcd(a, b) == 0. - Bézout's Identity
    # but the solutions can be negative (a, b can be negative)
    # but this problem does not allow us to order negative pizzas
    # so, just because gcd(a, b) divides c, does not mean there is a solution. we need to check if they are positive
    