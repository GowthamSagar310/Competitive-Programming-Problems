for _ in range(int(input())):
    n = int(input())
    arr = [0] * (2*n)
    index = 2*n
    for num in range(n, 0, -1):
        arr[index-1] = num
        temp = index-num
        while arr[temp-1] != 0:
            temp -= num
        arr[temp-1] = num
        index -= 1
    print(" ".join(map(str, arr)))
