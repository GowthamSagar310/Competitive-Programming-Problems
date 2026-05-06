for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    bs = [(val, i) for i, val in enumerate(arr, 1)]
    bs.sort()

    positions = [0] * (n+1)
    left_side = False
    left_max, right_max = 0, 0
    total = 0
    for i in range(n-1, -1, -1):
        times, building_num = bs[i]
        if left_side:
            positions[building_num] = left_max - 1
            left_max -= 1
        else:
            positions[building_num] = right_max + 1
            right_max += 1
        left_side = not left_side
        total += 2 * times * abs(positions[building_num])
    print(total)
    print(*positions)
