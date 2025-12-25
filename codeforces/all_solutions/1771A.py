for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    maxi, mini = max(arr), min(arr)
    

    # what if min == max

    if maxi == mini:

        # 1 1 1 1 1
        # there are n * (n-1) combinations
        # indexes (0, 1), (0, 2), (0, 3), (0, 4)
        #         (1, 2), (1, 3), (1, 4)
        #         (2, 3), (2, 4)
        #         (3, 4)
        # and reverse of all of these

        print(((n)*(n-1)))
    else:    
        # choose 1 from min_count group (min_count C 1) = min_count
        # choose 1 from max_count group (max_count C 1) = max_count 
        # interchange their positions (doubles the combinations)

        max_count, min_count = arr.count(maxi), arr.count(mini)
        print(2 * min_count * max_count)
