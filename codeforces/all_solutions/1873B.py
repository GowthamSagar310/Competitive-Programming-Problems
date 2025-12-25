from math import prod
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    # zeroes = arr.count(0)
    # if zeroes > 1:
    #     print(0)
    # elif zeroes == 1:
    #     arr[arr.index(0)] = 1
    #     print(prod(arr))
    # else:
    #     m = min(arr)
    #     print(prod(arr) // m * (m+1))

    arr.sort()
    arr[0] += 1
    print(prod(arr))