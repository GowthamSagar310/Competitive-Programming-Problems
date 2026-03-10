for _ in range(int(input())):
    n = int(input())

    # req = [6,2,5,5,4,5,6,3,7,6]
    # for 0 -> 6 segments are needed. and so on.
    # there 2, 3, 4, 5, 6, 7 in the above the array
    # meaning, 2a + 3b + 4c + 5d + 6e + 7f = n
    # if n % 2 == 0 -> use all 2 (maximizes the number of digits, which is 1)
    # if n % 2 == 1 -> let k = n // 2, use k-1 2s and 1 3 (which is 7)
    # this always maximizes the number of digits, so the number
    
    if n % 2 == 0:
        k = n // 2
        print("1"*k)
    else:
        k = (n // 2)-1
        print("7" + "1"*k)
