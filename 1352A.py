for _ in range(int(input())):
    n = int(input())
    ans = []
    
    i = 1
    while n:
        d = n % 10
        n //= 10
        if d: ans.append(str(d * (10 ** (i-1))))
        i += 1

    print(len(ans))
    print(" ".join(ans))