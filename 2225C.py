for _ in range(int(input())):
    n = int(input())
    r1 = input()
    r2 = input()
    i, j = 0, 0
    ops = 0
    while i < n:
        if r1[i] == r2[j]:
            i += 1
        elif i+1 < n and r1[i] == r1[i+1]:
            i += 2
        else:
            ops += 1
            i += 2
        if i-j > 1:
            if r2[j:j+2] == "BR" or r2[j:j+2] == "RB":
                ops += 1
        j = i
    print(ops)