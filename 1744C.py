for _ in range(int(input())):
    n, current = input().split()
    n = int(n)
    lights = input() * 2
    maximum = 0
    next_g = -1
    for i in range(n):
        if lights[i] == current:
            if i > next_g:
                j = i
                while j < 2*n:
                    if lights[j % n] == "g":
                        next_g = j
                        maximum = max(maximum, j-i)
                        break
                    j += 1
    print(maximum)