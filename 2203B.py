for _ in range(int(input())):
    num = input()

    s = 0
    digits = []
    for i, c in enumerate(num):
        s += int(c)
        digits.append((c, i))

    digits.sort()
    if s <= 9:
        print(0)
    else:
        diff = s-9
        ops = 0
        for i in range(len(num)-1, -1, -1):
            val, index = digits[i]
            if index == 0:
                can_remove = min(diff, int(val)-1)
            else:
                can_remove = min(diff, int(val))
            diff -= can_remove
            ops += 1
            if diff <= 0:
                break
        print(ops)