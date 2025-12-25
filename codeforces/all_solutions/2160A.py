def solve(arr):
    # in a valid partition all MEX are equal
    # get the minimum over all partitions

    # what is the minimum MEX possible parition ?
    # can we construct it ? 

    # if there is no 0, then each individual number can be a set -> MEX 0
    # if there is 0, then everything needs to be a single set for MEX to be same
    # and MEX of this, least integer which is not present. 

    arr.sort()
    for i in range(n):
        prev = -1 if i == 0 else arr[i-1]
        curr = arr[i]
        if curr-prev > 1:
            return prev+1
    return arr[-1]+1


    # another solution
    # we just have to check if 
    # 0 is present in array, if yes, move to 1, if yes, move to 2 
    # till, n + 1
    # because in array of length 5, in ideal scenario
    # [0, 1, 2, 3, 4] can be present, if any of them are not present,
    # they would be caught before hand, meaning
    # if the array is [100, 100, 100, 100] -> 0 will be caught
    # if the array is [0, 100, 100, 200] -> 1 will be caught
    # so the if [0, 1, 2, 3, 4] are not present -> it will n+1

    # O(N^2)
    # for i in range(0, n+1):
    #     if i not in arr:
    #         return i

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr))
