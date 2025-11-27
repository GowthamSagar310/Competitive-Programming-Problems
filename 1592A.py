for _ in range(int(input())):
    n, h = map(int, input().split())
    arr = list(map(int, input().split()))
    
    arr.sort()
    max1, max2 = arr[-1], arr[-2]
    if max1 >= h:
        print(1)
    else:
        total = (h // (max1 + max2)) * 2
        decrease = (h // (max1 + max2)) * (max1 + max2)
        h -= decrease
        if h <= 0:
            print(total)
        else:
            if h > max1: 
                total += 2
            else:
                total += 1
            print(total)        
    