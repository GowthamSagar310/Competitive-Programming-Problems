for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    updated = [False] * m
    for val in arr:
        min_index = min(val, m + 1 - val)
        if not updated[min_index-1]:
            updated[min_index-1] = True
        else:

            # if min_index == x
            # other index = m + 1 - x

            # if min_index == m + 1 - x
            # other_index ? x

            updated[m + 1 - (min_index) -1] = True
    print("".join("A" if b else "B" for b in updated))