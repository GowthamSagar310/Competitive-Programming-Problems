for _ in range(int(input())):
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    mini, maxi = arr[0], arr[-1]
    if mini <= s <= maxi:
        minimum_double_distance = min(s-mini, maxi-s)
        distance = maxi-mini + minimum_double_distance
    else:
        if s < mini:
            distance = maxi - s
        else:
            distance = s - mini
    print(distance)