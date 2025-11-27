for _ in range(int(input())):
    l, r = map(int, input().split())

    # the best way to construct is to
    # start from l and difference as 1 and keep increasing the difference
    # l, l+1, l+3, ... r

    # the pattern here is, the difference keeps increasing in form of
    # 1, 2, 3 .. d terms
    # sum of this is (d * (d + 1)) // 2
    # what is the maximum value of above expression that can fit in (r-l) ? 

    # the minimum possible value for number of terms = 1 
    # the maximum possible value for number of terms ? 
    
    # maximum difference according to problem = 10^9-1
    # (d * (d + 1)) // 2 <= 10^9 - 1
    # (d * (d + 1)) // 2 < 10^9
    # (d * (d + 1)) < 2 * 10^9
    # d ^ 2 + d < 2 * 10^9
    # d ^ 2 < 2 * 10^9
    # d < root (2 * 10 ^ 9)
    # d < 1.414 * sqrt(10) * 10000
    # d < 14140 * 3
    # d < 15000 * 3 (safe to assume)


    # please do note that the array does not have to end at exactly r
    mini, maxi = 1, 45000
    while mini <= maxi:
        mid = (mini + maxi) >> 1
        difference = (mid * (mid + 1)) // 2
        if difference > (r - l):
            maxi = mid-1
        else:
            mini = mid+1
    print(mini)

 