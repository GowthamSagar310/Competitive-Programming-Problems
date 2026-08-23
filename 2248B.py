for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    """
    1. choose two elements x <= y 
    2. delete and these and insert z which is x <= z <= y
    3. is it possible to make a == b after arrange "a" in any order

    1 4 5 6 10 90 100
    
    """