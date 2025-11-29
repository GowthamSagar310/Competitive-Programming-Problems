for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    # i < j
    # ai = ai + aj
    # aj = 0

    # min(a1) + min(a1, a2) + min(a1, a2, .. an)

    # you want the minimum to be involved in most of the minimum operations.
    # a1 is the most repeated and then 
    # a2 etc

    # 1 2 3 4 5 (increasing)
    # 1 1 1 1 1 = 5 
    # 1 1 0 0 0 = 2

    # 2 3 1 4 5 
    # 2 2 1 1 1 = 7
    # 3 3 0 0 0 = 6
    # 2 2 0 0 0 = 4
    
    # 3 2 1 4 5 
    # 3 2 1 1 1 = 8
    # 5 0 0 0 0 = 5
    
    # 5 4 3 2 1
    # 5 4 3 2 1 = 15
    # 9 0 0 0 0 = 9
    # 5 5 0 0 0 = 10

    # 3 0 2 3
    # 3 0 0 0 = 3

    # 3 3 3 3 3 
    # 3 3 3 3 3 = 15
    # 6 0 0 0 0 = 6
    # 3 3 0 0 0 = 6

    # 6 3 2 1 10
    # 6 3 2 1 1 = 13
    # 9 0 0 0 0 = 9

    # 1 10 2 3 4 5
    # 1  1 1 1 1 1 = 6
    # 1  1 0 0 0 0 = 2
    
    # make an early zero if possible
    if arr[0] <= arr[1]:
        print(arr[0] * 2)
    else:
        print(arr[0] + arr[1])