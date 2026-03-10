from math import isqrt
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
for i in range(n-1, -1, -1):
    if arr[i] >= 0:
        x = isqrt(arr[i])
        if x * x != arr[i]:
            print(arr[i])
            break
    else:
        print(arr[i])
        break
