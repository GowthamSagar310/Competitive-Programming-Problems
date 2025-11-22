for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr_with_index = [(arr[i], i) for i in range(n)]
    arr_with_index.sort()
    if arr_with_index[0][0] != arr_with_index[1][0]: print(arr_with_index[0][1]+1)
    else: print(arr_with_index[-1][1]+1)