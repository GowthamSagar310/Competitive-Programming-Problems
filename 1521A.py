for _ in range(int(input())):
    a, b = map(int, input().split())
    
    """
    - find three positive integers. x, y, z
    - x + y = z

    - one of them should be divisible by a*b
    - two of them should be divisible by only a.
    
    x = k1 (a)
    y = k2 (a)

    x+y = k1a + k2a
    
    x+y = a(k1 + k2)
    z = a * b
    
    a(k1 + k2) = a * b
    
    
    k1 + k2 = b
    
    - a % b == 0
    - "a" always contains b, so it wont be possible

    - a % b != 0
    k1 a + k2 a = k3 (a * b)
    
    13 2 

    k3 = 2 
    k1 + k2 = 4
    1 + 3 = 4
    
    13, 39, 52
    """
    if a % b == 0:
        print("NO")
    else:
        k2 = b-1 if b != 2 else 3
        k3 = 1 if b != 2 else 2
        print("YES")
        print(a, k2 * a, k3 * a * b)
