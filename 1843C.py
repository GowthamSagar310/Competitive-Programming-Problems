for _ in range(int(input())):
    n = int(input())

    # while traversing from top to bottom, 
    # we would not know which side to travel

    # but we kind of reverse the path
    # from n to 1
    # if n is odd, (n-1)// 2
    # if n is even, n // 2

    # because the children of node with value i
    # left -> 2*i
    # right -> 2*i+1

    node_val = n
    s = 1
    while node_val != 1:
        s += node_val
        node_val = (node_val-(node_val & 1)) // 2
    print(s)