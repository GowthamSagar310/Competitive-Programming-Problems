for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ones = arr.count(1)
    s = sum(arr) # including ones 
    if n == 1:
        print("NO")
    elif ones > n // 2 :
        if s - ones - (n - ones) >= ones:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
    """
    
    1. if there are less than half ones, then the whole array can be rearranged. 
    2. if there are more than half, we cannot rearrange them, we always have to increase them by 1
       but the other values should be able change themselves (decrease) to match the increased sum
       and also they cannot become zero themselves. 
    3. if there is only one element, we cannot do anything
    """
