for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    # when we add a smaller number to a larger number
    # we always bring the average down

    # so it is always the maximum

    print(max(arr))