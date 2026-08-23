for _ in range(int(input())):
    n, k = map(int, input().split())
    coordinates = []
    for _ in range(n):
        x, y = map(int, input().split())
        coordinates.append((x, y))


    """
    - find the minimum number of operations to bring everything into a single point
    
    - it seems reasonable to me to start from the biggest and close in into the center coordinates
    
    """

    coordinates.sort(key= lambda k: (k[0]) ** 2 + (k[1]) ** 2)
    for i in range(n):
        # can i mix coordinates[i] be a center
        possible = True
        x1, y1 = coordinates[i]
        for j in range(n):
            if i != j:
                x2, y2 = coordinates[j]
                if abs(x1-x2) + abs(y1-y2) > k:
                    possible = False
                    break
        if possible: break

    if possible:
        print(1)
    else:
        print(-1)
