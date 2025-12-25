for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    # if everything is equal cannot do it.
    # else, just take [1..n-1][n]
    # arr is sorted, so if first and last are equal, 
    # everything is equal

    if arr[0] == arr[-1]:
        print("NO")
    else:

        # we cannot use "R" * (n-1) + "B"
        # if 1 and n-1 elements are equal, R range would be 0
        # and also B range is 0 

        print("YES")
        print("R" * (n-2) + "BR")

