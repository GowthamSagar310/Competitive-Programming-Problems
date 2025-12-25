for _ in range(int(input())):
    n = int(input())
    
    # x 
    # y = x * 10^k
    # n = x + x * 10^k
    # n = x (1 + 10^k)
    
    # k = 1, n = 11 * x
    # k = 2, n = 101 * x

    ans = []    
    k = 1
    multiplier = 1 + 10 ** k
    while n >= multiplier:
        if n % multiplier == 0:
            ans.append(str(n // multiplier))
        k += 1
        multiplier = 1 + 10 ** k
    print(len(ans))
    if ans:
        print(" ".join(ans[::-1]))