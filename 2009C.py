for _ in range(int(input())):
    x, y, k = map(int, input().split())
    max_x, max_y = (x+k-1)//k, (y+k-1)//k
    total_steps = 2 * max(max_x, max_y)
    if max_x <= max_y:
        print(total_steps)
    else:
        print(total_steps-1)
