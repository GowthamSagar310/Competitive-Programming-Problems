from math import ceil
for _ in range(int(input())):
    n, x, y, z = map(int, input().split())

    """
    nikita-no-ai = ceil(n/(x+y))
    nikita-with-ai = ceil(n - (z * x)/(x + y*10))
    """
    # without ai
    nikita_no_ai = ceil(n/(x+y))
    
    # with_ai
    if n > z * x:
        nikita_with_ai = z + ceil((n- z*x) / (x + 10*y))
    else:
        nikita_with_ai = ceil(n / x)
    
    print(max(1, min(nikita_no_ai, nikita_with_ai)))
    