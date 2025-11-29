for _ in range(int(input())):
    
    a, b, n = map(int, input().split())

    # minimum number of times you have to move the mouse ?
    # minimum number of times the length changes ? 

    # if b < a 
    # the size of each tab can grow only till b
    # we move the end, close all the tabs, tab length is b
    # and move to the start and close them all
    # two moves 

    # if b >= a
    # tabs are always going to spread out. 
    # we can close them all by just being at the end

    # if b >= a -> tabs are always going end at one position
    # if b < a
    #   if b * n <= a -> start at the beginning 
    #   if b * n > a -> start at end close few, come back to start and close them all.

    if b >= a or (n * b <= a):
        print(1)
    else:
        print(2)