for _ in range(int(input())):
    n = int(input())
    s = list(map(int, list(input())))
    total = sum(s)

    """
    1. sum should be even by number should be odd. 
    - remove all the even numbers from the end. 
    - if the sum is not still divisible by 2, remove odd numbers from n-2 to 0
    """

    while s and s[-1] % 2 == 0:
        total -= s[-1]
        del s[-1]
    
    if not s: 
        print(-1)
    elif total % 2 == 0:
        print("".join(map(str, s)))
    else:
        for i in range(len(s)-2, -1, -1):
            if s[i] & 1:
                total -= s[-1]
                del s[i]
                break
        print("".join(map(str, s)) if (s and total % 2 == 0) else -1)
