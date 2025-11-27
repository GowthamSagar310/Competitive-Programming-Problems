from functools import reduce
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    # we need to try to take the bits from smaller numbers 
    # and give them to biggest number

    # construct max
    # bit pos 0 -> [1, 1, 1, 1, 0, 1, 1]
    # meaning some number has a 1 in it at pos 0
    # we can take it into maximum number
    # likewise we can construct every bit in maximum number
    # if everything is 0, we cannot take it
    # OR

    # construct min
    # bit pos 1 -> [1, 1, 0, 1, 1, 1]
    # meaning some number has a 0 in it at pos 1
    # and we can take it into minimum number
    # if everything is 1, we cannot take it.
    # AND

    total_or = reduce(lambda i, j: i | j, arr, arr[0])
    total_and = reduce(lambda i, j: i & j, arr, arr[0])

    print(total_or - total_and)

