for _ in range(int(input())):
    m, n = map(int, input().split())
    maxi = 0
    for r in range(m):
        row = input()
        left_index = row.find("#")
        right_index = row.rfind("#")
        if left_index != -1:
            if right_index - left_index + 1 > maxi:
                maxi = right_index - left_index + 1
                x = r + 1
                y = ((left_index + right_index) // 2) + 1
    print(x, y)