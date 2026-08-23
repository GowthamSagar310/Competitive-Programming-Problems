for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = []
    for i in range(n):
        greater = lesser = 0
        for j in range(i+1, n):
            if arr[i] < arr[j]: greater += 1
            elif arr[i] > arr[j]: lesser += 1
        ans.append(max(greater, lesser))
    print(*ans)