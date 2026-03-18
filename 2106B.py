for _ in range(int(input())):
    n, x = map(int, input().split())

    """
    permutation of 0 to n-1
    
    4, 2
    0 1 3 2

    4, 0
    1 2 3 0

    3 3
    0 1 2

    4 3
    0 1 2 3
    """
    
    ans = list(range(0, x))
    ans.extend(list(range(x+1, n)))
    if len(ans) != n: ans.append(x)
    
    print(*ans)