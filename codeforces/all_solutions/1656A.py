for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    # arr_with_index = sorted([(arr[i], i) for i in range(n)])
    # min_index, max_index = arr_with_index[0][1], arr_with_index[-1][1]
    # print(min_index+1, max_index+1)

    mini_index, mini = -1, float("inf")
    maxi_index, maxi = -1, float("-inf")

    for i in range(n):
        num = arr[i]
        if num < mini:
            mini_index = i+1
            mini = num
        if num > maxi:
            maxi_index = i+1
            maxi = num
        
    print(mini_index, maxi_index)