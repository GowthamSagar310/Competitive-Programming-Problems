for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    """
    1. if the total sum of the arr is 0, the last prefix sum is always zero. not possible
    2. if total > 0, that means the last prefix sum will always be greater than zero. 
       so, if we arrange all the positive values up front, it can never come back to zero at end
    3. if total < 0, that means the last prefix sum will always be less than zero
       so, if we arrange all the negative values first, it can never go up to zero at end.
    """
    total = sum(arr)
    if total == 0:
        print("NO")
    elif total > 0:
        print("YES")
        print(*sorted(arr, reverse=True))
    else:
        print("YES")
        print(*sorted(arr))