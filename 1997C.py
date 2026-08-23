for _ in range(int(input())):
    n = int(input())
    s = input()
    previous_open = [0]
    count = 1
    cost = 0
    for i in range(1, n):
        if i % 2 == 0:
            if count:
                last_open_bracket = previous_open.pop()
                cost += (i - last_open_bracket)
                count -= 1
            else:
                previous_open.append(i)
                count += 1
        else:
            if s[i] == "(":
                count += 1
                previous_open.append(i)
            else:
                last_open_bracket = previous_open.pop()
                cost += (i - last_open_bracket)
                count -= 1
    print(cost)