import math
for _ in range(int(input())):
    n = int(input())

    if n % 2:
        print(-1)
        continue

    seq = []
    while n > 1:
        p1 = (n-1) // 2
        p2 = (n+1) // 2
        if p1 % 2 == 1:
            seq.append(1)
            n = p1
        else:
            seq.append(2)
            n = p2
    
    if len(seq) > 40:
        print(-1)
    else:
        seq.reverse()
        print(len(seq))
        print(*seq)