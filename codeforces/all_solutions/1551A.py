for _ in range(int(input())):
    n = int(input())

    # c1 * 1 + c2 * 2 = n

    # if c1 = c2, abs(c1-c2) = 0, n % 3 == 0
    # if n % 3 == 1, c1=c1+1, c2, abs(c1-c2)=1
    # if n % 3 == 2, c2=c2+1, abs(c1-c2)=1
    
    c1 = (n // 3) + (1 if n % 3 == 1 else 0)  
    c2 = (n // 3) + (1 if n % 3 == 2 else 0)

    print(c1, c2)
