for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    s = sum(arr)
    if s >= n:
        print(s-n)
    else:
        # make the average >= 1

        # what is the one value that can be added to s 
        # to make the average = 1
        # s + x = n + 1
        # x = n + 1 - s
        
        print(1)