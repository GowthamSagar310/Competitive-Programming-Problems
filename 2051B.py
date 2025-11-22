# for _ in range(int(input())):
#     n, a, b, c = map(int, input().split())

    # 0 - a 
    # 1 - b
    # 2 - c
    # 3 - a
    # 4 - b
    # .
    # .
    # .

    # how many complete cycles ?
    # n // (a + b + c)
    
    # total_cycles = n // (a + b + c)
    # total_days = total_cycles * 3
    # remaining = n % (a + b + c)
    # if remaining == 0:
    #     print(total_days)
    # elif remaining-a <= 0:
    #     print(total_days + 1)
    # elif remaining-(a+b) <= 0:
    #     print(total_days + 2)
    # else:
    #     print(total_days + 3)


# this problem is tagged as binary search, but it is not that intuitive

def walked(days, a, b, c):
    cycles = days // 3
    remaining_days = days % 3
    total = cycles * (a + b + c)
    if remaining_days == 1:
        total += a
    elif remaining_days == 2:
        total += (a + b)
    return total

for _ in range(int(input())):
    n, a, b, c = map(int, input().split())
    # find the number of days using binary search
    # l = 1 -> we atleast need one day
    # h = n -> worst case in which we walk 1km/day

    l, h = 1, n
    ans = n
    while l <= h:
        mid = (l + h) >> 1
        if walked(mid, a, b, c) >= n:
            # for "mid" days, we walked more than n
            # try smaller number of days
            ans = mid
            h = mid-1
        else:
            # we need to walk more
            l = mid+1
    print(ans)