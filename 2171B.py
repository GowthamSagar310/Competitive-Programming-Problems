for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    """
    only the ends matter. 
    everything else in the middle gets cancelled. 
    """

    if arr[0] != -1 and arr[-1] != -1:
        print(abs(arr[-1]-arr[0]))
    else:
        print(0)
        m = max(arr[0], arr[-1])
        arr[0] = arr[-1] = m 
    print(*map(lambda x: max(x, 0), arr))