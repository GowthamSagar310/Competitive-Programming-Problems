for _ in range(int(input())):
    n, j, k = map(int, input().split())
    arr = list(map(int, input().split()))
    maxi = max(arr)
    if k == 1:
        if arr[j-1] == max(arr):
            print("YES")
        else:
            print("NO")
    else:
        print("YES")