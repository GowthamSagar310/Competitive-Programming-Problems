for _ in range(int(input())):
    n = int(input())

    maximum = 1
    a = [4, 6, 2, 0, 8, 9, 1, 3, 5, 7]
    for i in range(1, n):
        maximum = max(maximum, a[i-1] ^ a[i])
    
    print(maximum)

    maximum = 1
    a = [4, 6, 3, 2, 0, 8, 9, 1, 7, 5]
    for i in range(1, n):
        maximum = max(maximum, a[i-1] ^ a[i])
    print(maximum)