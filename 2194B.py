for _ in range(int(input())):
    n, x, y = map(int, input().split())
    arr = list(map(int, input().split()))

    # idea here is that put more coins into a value
    # which when used for transfer will have more left over coins (which cannot be used)
    # so move coins into that value. 

    # but it wont work because
    # we are transfering value from initial maximum value
    # because of that we are loosing the value by x-y
    # if this happens multiple times, we are reducing the possible maximum

    # that is why we need to prove our solutions always
    # arr.sort(key= lambda val: val % x)
    # for i in range(n-1):
    #     arr[-1] += y * (arr[i] // x)
    # print(arr[-1])

    # there is one maximum value
    # to which everything will be coming to at alast. (there is only one)
    # so, except for sum([arr[i]//x for all values]) - except for the current value
    # so far values, if we can find the max of these, we should be good.

    total = sum(val//x for val in arr)
    maximum = 0
    for val in arr:
        maximum = max(maximum, val + y * (total - (val // x)))
    print(maximum)