for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    total = sum(arr)
    """
    - 
    """
    if total % 2 == 1:
        print("YES")
    else:
        if (n * k) % 2 == 0:
            print("YES")
        else:
            print("NO")