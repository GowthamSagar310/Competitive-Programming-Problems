for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    # index of smallest = si
    # index of largest = li
    # middle index = mi

    # if both si, li are on same side of mi, remove from one side
    # if they are on opposite sides, go from oppsite side

    si = arr.index(min(arr))
    li = arr.index(max(arr))
    mi = (n-1)// 2

    # this logic fails because 
    # [3, 2, 1, 5, 9, 6, 7]
    # minimum is 6, but because of this middle index strategy, 
    # we are not considering how far apart, si and li are.

    # if si <= mi and li <= mi:
    #     # cut from left side
    #     print(max(si, li) + 1)
    # elif si >= mi and li >= mi:
    #     # cut from right side
    #     print(n-min(si, li))
    # else:
    #     # cut from both sides
    #     if si < li:
    #         print(si+1+(n-li))
    #     else:
    #         print(li+1+(n-si))

    # instead of heuristic, the ans values remain unchanged,
    # so we can just take minimum of all those 

    print(min(
        max(si, li) + 1,
        n-min(si, li),
        min(si,li)+1+(n-max(si, li))
    ))
