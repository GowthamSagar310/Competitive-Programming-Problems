def solve(arr, f, a, b):
    # it only makes sense to turn off and on,
    # if cost of keep phone on > off and on
    # (difference) * a > b

    current = 0
    for mt in arr:
        time_diff = mt-current
        if time_diff * a > b:
            # turn off and on
            charge_lost = b
        else:
            # keep it on
            charge_lost = time_diff * a
        if charge_lost >= f:
            return False
        f = f - charge_lost
        current = mt
    return True

for _ in range(int(input())):
    n, f, a, b = map(int, input().split())
    arr = list(map(int, input().split()))
    print("YES" if solve(arr, f, a, b) else "NO")


