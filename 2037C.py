for _ in range(int(input())):
    n = int(input())

    """
    - permuation for n numbers
    - pi + pi+1 should be a composite
    
    
    - any two numbers with same parity, produces a even number -> which is composite (>2 ofcourse)
    - how to mix odd an even numbers ? 
    - 4 + 5 is one of the case of different partiy which produces a compisite (9)
    - even numbers + 4 + 5 + odd numbers
    
    if n < 5: return -1
    """

    if n < 5:
        print(-1)
        continue

    for i in range(2, n+1, 2):
        if i != 4:
            print(i, end = " ")
    
    print("4 5", end = " ")

    for i in range(1, n+1, 2):
        if i != 5:
            print(i, end = " ")