for _ in range(int(input())):
    a, b = map(int, input().split())
    
    # a + a, b
    a1 = max(a+a, b) * max(a+a, b)

    # b + b, a
    a2 = max(a, b+b) * max(a, b+b)

    print(min(a1, a2))