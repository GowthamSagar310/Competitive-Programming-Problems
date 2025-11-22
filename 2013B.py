for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    # the last element is left alone
    # make the elements indexed from [0, n-2] as negative as possible 
    # reduce the max of these values. 

    print(arr[-1]-(arr[-2]-sum(arr[:-2])))