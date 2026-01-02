for _ in range(int(input())):
    n, m, i, j = map(int, input().split())

    # we want him to move
    # horizontally twice and vertically twice
    # so placing at opposite corners works. 
    # even if anton is in one of the corner, he always has to go back
    
    print(*[1, 1, n, m])