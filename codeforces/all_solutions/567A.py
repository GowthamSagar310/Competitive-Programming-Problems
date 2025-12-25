n = int(input())
arr = list(map(int, input().split()))

for i in range(n):

    left = right = float("inf")
    if i > 0: left = arr[i]-arr[i-1]
    if i < n-1: right = arr[i+1]-arr[i]

    # what if there is only one city ? it does not make sense. 

    leftmost = arr[i]-arr[0]
    rightmost = arr[n-1]-arr[i]
    print(min(left,right), max(leftmost, rightmost))