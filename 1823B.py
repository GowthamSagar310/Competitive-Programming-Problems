for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    # check if it possible to swap with k
    exchange_needed = 0
    for i in range(n):
        if i+1 != arr[i]: # must be swapped
            current_index, swap_index = i, arr[i]-1
            if abs(current_index - swap_index) % k == 0:
                # can be swapped.
                pass
            else:
                exchange_needed += 1

    if exchange_needed == 0:
        print(0)
    elif exchange_needed == 2:
        # for each exchange_needed, we can swap two elements
        # but since we are not exactly swapping, we will count two times
        # once for each of should be swapped element
        print(1)
    else:
        print(-1)