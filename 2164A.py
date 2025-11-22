for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    x = int(input())

    # if x is between min and max of arr, it is always possible
    # or else it is not 

    if min(arr) <= x <= max(arr):
        print("YES")
    else:
        print("NO")