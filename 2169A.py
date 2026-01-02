for _ in range(int(input())):
    n, a = map(int, input().split())
    arr = list(map(int, input().split()))   



    less = more = 0
    for val in arr:
        if val < a:
            less += 1
        elif val > a:
            more += 1

        # if val == a: 
        # there is nothing bob can do to maximize his points
        # except for val == a, we need to check how many values are less or more
        

    if less <= more:
        print(a+1)
    else:
        print(a-1)
