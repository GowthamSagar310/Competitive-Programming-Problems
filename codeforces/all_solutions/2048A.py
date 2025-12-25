for _ in range(int(input())):
    n = int(input())

    # op1: remove "33"
    # op2: subtract 33

    # for these kinds of problems, 
    # see if there is a relation between them
    # or if one can be transformed into another

    # original number = prefix * 10^(p+2) + 33 * 10^p + suffix
    # remove 1 "33" = prefix * 10^p + suffix
    # difference = 99 * 10^p * prefix + 33 * 10^p
    # difference = (99 * prefix + 33) * 10^p
    # this is clearly divisible by 33
    # that means when we are removing "33", we are actually
    # subtracting 33 some number of times 

    # so op1, and op2 are kind of same

    # now we just have to see if the number is divisible by 33
    # so that we either remove the "33" or -33 to make it zero

    print("YES" if n % 33 == 0 else "NO")

