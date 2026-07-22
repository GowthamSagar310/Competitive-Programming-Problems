for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    """
    
    - we will have to make it zig zag
    - b1 < b2 > b3 < b4 ... 
    - the relation constraint is only between adjacent elements. 
    
    - 65 85 19 53 21 79 92 29 96
    - 65 85 19 53 21 93 92 29 96 (1 op1 + 8 op2)
    - 65 85 19 53 21 93 92 97 96 (1 op1 + 4 op2)

    - 3 3 2 3
    - 2 3 2 3
    
    - 6 6 6 6 6
    - 5 6 6 6 6 op=1
    - 5 6 5 6 6 op=2
    - 5 6 5 6 6
    - 5 6 5 6 5 op=3
    """

    max_till_now = arr[0]
    for i in range(n):
        if i % 2 == 1:
            arr[i] = max(arr[i], max_till_now)
        max_till_now = max(max_till_now, arr[i])
    
    ops = 0
    for i in range(n-1):
        if i % 2 == 0 and arr[i] == arr[i+1]:
            arr[i] -= 1
            ops += 1
        elif i % 2 == 1 and arr[i] <= arr[i+1]:
            ops += arr[i+1]-arr[i]+1
            arr[i+1] = arr[i]-1
    print(ops)


