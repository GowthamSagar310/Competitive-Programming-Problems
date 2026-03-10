for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    # answer is either 0, 1, 2, 3
    flag = False
    for i in range(n):
        if i+1 != arr[i]:
            # requires either 1 or 2 or 3 operations
            flag = True
            break
    if not flag:
        print(0)
    else:
        if arr[0] == 1 or arr[-1] == n:
            print(1)
        elif arr[0] == n and arr[-1] == 1:
            print(3)
        else:
            print(2)